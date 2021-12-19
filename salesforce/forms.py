from django import forms


class SalesForceIntegrationForm(forms.Form):
    client_id = forms.CharField(label='Consumer Key')
    client_secret = forms.CharField(label='Consumer Secret')
    username = forms.CharField(label='Username')
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(),
        help_text='ex: (password+security token)'
    )