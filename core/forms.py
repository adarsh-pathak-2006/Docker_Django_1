from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    rep_password=forms.CharField(widget=forms.PasswordInput())

class LoginForm(ModelForm):
    class Meta:
        model=User
        fields=['username', 'password']
        