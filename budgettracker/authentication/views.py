from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login


class RegistrationView(View):
    def get(self,request):
        return render(request, 'authentication/register.html')
