from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('integarte-salesforce/', views.salesforce_integration, name='integrate_salesforce'),
    path('users/', views.UsersListView.as_view(),name='users_list_view'),
    path('accounts/', views.AccountsListView.as_view(), name='accounts_list_view'),
    path('contacts/', views.ContactListView.as_view(),name='contacts_list_view')
]
