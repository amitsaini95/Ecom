from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','password1','password2')
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
class LoginForm(AuthenticationForm):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())
    fields=('username','password')
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
