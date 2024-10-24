from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import LoginForm, ResetPasswordForm, SignupForm
from .models import CustomUser



class MyCustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)


        self.fields["login"] = forms.CharField(label='Username',required=False,widget=forms.TextInput(attrs={
            'placeholder': '账号',
            "id":"username",
            "name":"username",
            "class":"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
        }))

        self.fields["password"] = forms.CharField(label='Password', required=False,widget=forms.PasswordInput(attrs={
            'placeholder': '密码',
            "id":"password",
            "name": "password",
            "class":"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
        }))


class MyCustomRestPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomRestPasswordForm, self).__init__(*args, **kwargs)

        self.fields["email"] = forms.CharField(label='Username', required=False, widget=forms.TextInput(attrs={
            'placeholder': '账号',
            "id": "username",
            "name": "username",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
        }))


class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields["email"] = forms.CharField(label='Username', required=False, widget=forms.TextInput(attrs={
            'placeholder': '账号',
            "id": "username",
            "name": "username",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
        }))
        self.fields["password1"] = forms.CharField(label='Password', required=False, widget=forms.PasswordInput(attrs={
            'placeholder': '密码',
            "id": "password",
            "name": "password",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
        }))

        self.fields["password2"] = forms.CharField(label='Confirm password', required=False, widget=forms.PasswordInput(attrs={
            'placeholder': '确认密码',
            "id": "password",
            "name": "password",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
        }))

