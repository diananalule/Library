from django.shortcuts import render
from django.http import HttpResponse
from . import views
# Creating the views here.


def Login_view(request):
    return HttpResponse('Please login from here')


def Logout_view(request):
    return HttpResponse('please logout from here')


def Register_view(request):
    return HttpResponse('please register from here')