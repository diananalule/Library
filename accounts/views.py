from django.shortcuts import render
from django.http import HttpResponse
#from . import views
# Creating the views here.


def Login_view(request):
    return render(request,'accounts/index.html')


def Logout_view(request):
    return render(request,'accounts/logout_view.html')


def Register_view(request):
    return render(request,'accounts/register_view.html')