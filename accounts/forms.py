from django import forms
from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# from django.contrib.auth.models import AbstractUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    confirm_password = forms.CharField(
        max_length=128, widget=forms.PasswordInput())

    #!not working
    def clean_username(self):
        # username = self.cleaned_data['username']
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('Username is taken')
        return self.cleaned_data['username']
    #!not working

    #!not working
    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Your Passwords do not match")
     #!not working
