# from tkinter.tix import Select
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput, Select, Textarea, FileInput
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': "rounded-lg shadow-sm w-72 sm:w-auto dark:bg-slate-900",
                'placeholder': 'Username'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={
            'class': 'form_input',
            'placeholder': 'Password'})
        self.fields['password2'].widget = PasswordInput(attrs={
            'class': 'form_input',
            'placeholder': 'Confirm password'})


class Account(ModelForm):
    class Meta:
        model = Accounts
        exclude = ['user']
        widgets = {
            'profile_pic': FileInput(attrs={
                'class': "bg-slate-200 rounded-lg form_field_slide file:bg-slate-300 file:hover:bg-slate-400 file:cursor-pointer file:rounded-l-lg file:border-0 file:font-semibold file:py-2 shadow-sm file:border-l-2 file:border-slate-400 border-b-2 border-slate-300 file:pl-2 file:dark:bg-slate-500 dark:border-slate-400 file:dark:border-slate-500 dark:text-slate-900 font-semibold",
            }),
            'date_of_birth': TextInput(attrs={
                'class': "form_input form_field_slide",
                'placeholder': 'Date of birth'
            }),
            'email': TextInput(attrs={
                'class': "form_input form_field_slide",
                'placeholder': 'Email',
                'size': '40'
            }),
            'gender': Select(attrs={
                'class': "form_input form_field_slide",
                'placeholder': 'Gender'
            }),
            'about_you': Textarea(attrs={
                'class': "form_input form_field_slide",
                'placeholder': 'Tell us something about yourself here 😉'
            }),
            'status': TextInput(attrs={
                'class': "form_input form_field_slide",
                'placeholder': 'Status'
            })

        }


class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form_input mx-4',
             'placeholder': 'Username'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form_input mx-4',
             'placeholder': 'Password'}
        )
        