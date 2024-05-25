from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','password','password1')
class LoginForm(AuthenticationForm):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())
    fields=('username','password')
