from django import forms
from .models import *
class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    class Meta:
        model = Customer
        fields = ['username','password','email','full_name','region','town',]

        def clean_username(self):
            uname = self.cleaned_data.get(username)
            if User.objects.filter(username = umane).exists():
                raise forms.ValidationError('this username is already taken')
            return uname

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('this email is already taken')
            return email
