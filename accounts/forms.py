from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import LoginForm,ResetPasswordForm
from .models import CustomUser



class MyCustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)


        self.fields["login"] = forms.EmailField(label='username',required=False,widget=forms.TextInput(attrs={
            'placeholder': '账号',
            "id":"username",
            "name":"username",
            "class":"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
        }))

        self.fields["password"] = forms.CharField(label='password', required=False,widget=forms.PasswordInput(attrs={
            'placeholder': '密码',
            "id":"password",
            "name": "password",
            "class":"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
        }))


class MyCustomRestPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomRestPasswordForm, self).__init__(*args, **kwargs)

        self.fields["email"] = forms.EmailField(label='电子邮箱', required=False, widget=forms.TextInput(attrs={
            'placeholder': 'E-mail',
            "id": "username",
            "name": "username",
            "class": "mt-1 p-2 w-full border rounded-md focus:border-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-300 transition-colors duration-300"
        }))