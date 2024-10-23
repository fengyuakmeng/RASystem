from django.shortcuts import render

# Create your views here.

from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapters(DefaultAccountAdapter):

    def get_logout_redirect_url(self, request):
        path = "/about/"
        return path