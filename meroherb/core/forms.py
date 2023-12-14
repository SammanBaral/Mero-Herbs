from django import forms

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'overlap-group-2'

    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':'overlap-group-2'


    }))

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')

    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'overlap-group-3'

    }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email',
        'class':'overlap-group-2'

    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Retype Password',
        'class':'overlap-2'

    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':'overlap-group-3'

    }))

