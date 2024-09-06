from django import forms
from .models import Todo

#this importation of modules below is for the user authentication form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'details', 'completed'] 

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length = 250)


#this part of the form is a user creation form to add the authentication part to my program
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
            max_length = 100,
            required  = True,
            help_text = 'Enter Email Address',
            widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Email'}),
            )

    first_name = forms.CharField(
            max_length = 50,
            required = True,
            help_text = 'Enter First Name',
            widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'First Name'}),
            )

    last_name = forms.CharField(
            max_length = 50,
            required = True,
            help_text = 'Enter Last Name',
            widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Last Name'}),
            )

    username = forms.CharField(
            max_length = 50,
            required = True,
            help_text = 'Enter Username',
             widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Username'})
            )

    password1 = forms.CharField(
            max_length = 20,
            help_text = 'Enter Password',
            required = True,
            widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Password'}),
            )

    password2 = forms.CharField(
            max_length = 20,
            help_text = 'Enter Password',
            required = True,
            widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Confirm Password'}),
            )

    check = forms.BooleanField(required = True)



    class Meta:
        model = User
        fields = [
                'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'check',
                  ]