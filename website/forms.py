from django.contrib.auth.forms import UserCreationForm #creates users
from django.contrib.auth.models import User
from django import forms

#Class inherits from UserCreationForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name =  forms
    last_name =
