import itertools
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import ListView
from .forms import SalesForceIntegrationForm
from . import helper, models
# Create your views here.

def home(request):
    """
    If all counts values are zero, which means first not made yet or
    we did all of requests are failed for some reason.
    If any of the case is true then that user will be redirected to 
    Salesforce integration page to provide the credentials.
    """
    counts = {
        'users': models.SalesForceUser.objects.all().count(),
        'accounts':models.SalesForceAccount.objects.all().count(),
        'contacts':models.SalesForceContact.objects.all().count()
    }
    
    if not any(counts.values()):
        return redirect(salesforce_integration)
    return render(request, 'salesforce/home.html', context=counts)


def salesforce_integration(request):
    """
    This function based view is used for getting salesforce credentials.
    
    That credentials will be used to get access_token from salesfroce
    using oauth2 authentication.

    Then with that token users, accounts and contacts data
    will be fetched and stored into the database.
    """
    form = SalesForceIntegrationForm()
    if request.method == 'POST':
        form = SalesForceIntegrationForm(request.POST)
        
        if form.is_valid():
           # ORDER IS MATTER HERE IN THE LIST
            credentials = dict(
                zip(['username', 'password', 'client_id', 'client_secret'],  # ORDER IS MATTER HERE
                itertools.cycle(['']))
            )

            for _  in credentials:
                credentials[_] = form.data.get(_)    
            
            # if credentials is valid it will return dict with access_token and instance url 
            # else return empty dict.
            salesforce = helper.SalesForce(*credentials.values())
            messages.success(request, 'Fetching.... please wait!')
            
            if salesforce.auth():
                # if authenticated the request will be made and stored to database
                salesforce.fetch_and_store_to_database()
                messages.success(request, 'Successfully fetched data from salesforce!')
                return redirect(home)
            
            else:
                messages.warning(request, 'There is issue in your credentials!')
        
        else:
            messages.warning(request, 'The is issue in your form submission!')
    
    return render(request, 'salesforce/integrate_salesforce.html',context={'form':form})


class UsersListView(ListView):
	template_name = 'salesforce/users.html'
	model = models.SalesForceUser
	context_object_name = 'users' 


class AccountsListView(ListView):
	template_name = 'salesforce/accounts.html'
	model = models.SalesForceAccount
	context_object_name = 'accounts' 


class ContactListView(ListView):
	template_name = 'salesforce/contacts.html'
	model = models.SalesForceContact
	context_object_name = 'contacts' 
