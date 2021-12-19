from django.db import models

# Create your models here.



class SalesForceUser(models.Model):
    salesforce_id = models.CharField(max_length=64, unique=True)
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length=128, null=True, blank=True)
    firstname = models.CharField(max_length=128, null=True, blank=True)
    lastname = models.CharField(max_length=128, null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    mobile = models.CharField(max_length=32, null=True, blank=True)
    company_name = models.CharField(max_length=128, null=True, blank=True)
    # address are dict types but that will stored as string
    # can be loaded as string in future use
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.salesforce_id} | {self.name}"


class SalesForceAccount(models.Model):
    salesforce_id = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    account_number = models.CharField(max_length=128, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    annual_revenue = models.CharField(max_length=32, null=True, blank=True)
    # address are dict types but that will stored as string
    # can be loaded as string in future use
    billing_address = models.TextField(null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.salesforce_id} | {self.name}"


class SalesForceContact(models.Model):
    salesforce_id = models.CharField(max_length=64,unique=True)
    firstname = models.CharField(max_length=128, null=True, blank=True)
    lastname = models.CharField(max_length=128, null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    account_id = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(max_length=128, null=True, blank=True)
    mobile_phone = models.CharField(max_length=32, null=True, blank=True)
    mailing_address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.salesforce_id} | {self.name}"