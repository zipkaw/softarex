from django import forms
from django.core.exceptions import ValidationError

from .models import RestaurantData

class RegistryUser(forms.Form):
    username = forms.CharField(max_length=30, label='Your name')
    password = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50, label='Retry password input', widget=forms.PasswordInput())
    
    def clean_password_data(self):
        data = self.cleaned_data['password']
        if data['password'] != data['password2']:
            raise ValidationError(('Password does not match'))
        if len(data['password']) < 8: 
            raise ValidationError(('Minimal size of password must be geater than 8 characters'))
        return data

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')

class UpdateNameForm(forms.Form):
    new_name = forms.CharField(label='New Name', max_length=100)

class RestUploadForm(forms.ModelForm):
    class Meta:
        model = RestaurantData
        exclude = (
            'user',
            'revenue'
            )