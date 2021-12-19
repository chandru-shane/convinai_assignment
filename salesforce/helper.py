import requests
from . import models
from . import utils




class SalesForce:

    _mapping_models_fields = {
        'users': (models.SalesForceUser, utils.USER_FIELDS), 
        'accounts': (models.SalesForceAccount, utils.ACCOUNT_FIELDS),
        'contacts': (models.SalesForceContact, utils.CONTACT_FIELDS)
    }

    def __init__(self, username:str, password:str, client_id:str, client_secret:str):
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret
        self.is_auth = False
    

    def auth(self):
        """
        This method authenticate the instance with the credentials and 
        sets the headers, access_token, instance_url, oauth_response_json
        as instance attribute.
        And sets is_auth to True if authenticated properly.
        """
        params = {
        'grant_type':'password',
        'username': self.username,
        'password': self.password,
        'client_id': self.client_id,
        'client_secret': self.client_secret
        }
        self.auth_response = requests.post('https://login.salesforce.com/services/oauth2/token', params=params)


        if self.auth_response.status_code == 200:
            
            self.oauth_response_json = self.auth_response.json()
            self.access_token = self.oauth_response_json.get('access_token')
            self.instance_url = self.oauth_response_json.get('instance_url')
            
            self.is_auth = True
            
            self.headers = {
                'Authorization': f'Bearer {self.access_token}'
            }
            
            
            return {
                'access_token':  self.access_token,
                'instance_url': self.instance_url
            }

        else:
            return {}
    
    def authenticate(self):
        """
        If instance is not authenticated then instance will authenticte.
        """
        if not self.is_auth:
            self.auth()

    def fetch(self, url):
        """
        fetch method fetch the data from url and return data as list.
        """
        self.authenticate()
        
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise ValueError(f'{response.json()}')

        # records = deepcopy(response.json().get('records'))
        records = []
        for record in response.json().get('records'):
                records.append(record)
        
        # this code is for managing and makeing paginated request 
        # to get full data
        # not faced this scenario may go raise error
        try:
            while not response.json().get('done'):
                if not response.json.get('nextRecordsUrl', False):
                    break
                else:
                    response = requests.get(response.json.get('nextRecordsUrl'), headers=self.headers)
                    for record in response.json().get('records'):
                        records.append(record)
        except Exception as ex:
            print(ex)
       
        return records

    def _parse_create(self, model, data, fields):
        """
            This is more generic function.
        

        Args:
            model (type): [django model subclass where need to stored]
            data (dict): [data have to be stored in model]
            fields (dict): [fields have data and database field names]

        Returns:
            model type: [if object exists with same
                Id then that will be retirve and return or 
                create new one and retrun.
        """
        try:
            obj, created = model.objects.get_or_create(
            salesforce_id=data.get('Id')
            )

            if created:
                for key, value in fields.items():
                    setattr(obj, value, data.get(key))
                obj.save()
        except Exception as ex:
            print(ex)

        return obj
    
    def _parse_and_create(self,model, data, fields):
        return self._parse_create(model,data, fields)    


    def store_to_databases(self,all_records:dict):
        """
        This method takes care of storing into database.
        """
        for record_name, records in all_records.items():
            for record in records:
                self._parse_and_create(
                    SalesForce._mapping_models_fields.get(record_name)[0],
                    record,
                    SalesForce._mapping_models_fields.get(record_name)[1],
                )
    

    
    def fetch_data(self):
        """
        This method takes care of fetching and return the dicts of data.
        """
        query_url = f"{self.instance_url}/services/data/v45.0/query?q="
        url_endpoints = {
            'users':f"{query_url}SELECT {','.join(utils.USER_FIELDS.keys())}  FROM user ",
            'accounts':f"{query_url}SELECT {','.join(utils.ACCOUNT_FIELDS.keys())} FROM account ",
            'contacts':f"{query_url}SELECT {','.join(utils.CONTACT_FIELDS.keys())} FROM Contact",
        }
        result = {}
        for key,value in url_endpoints.items():
            result[key] = self.fetch(value)
        return result
    
    
    def fetch_and_store_to_database(self):
        """
        This method takes care of fetching and 
        storing to the database.
        """
        all_records = self.fetch_data()
        self.store_to_databases(all_records)
        return all_records
    
    
