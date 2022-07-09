from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def home(request):
    return render(request,"accounts/index.html")

def about_view(request):
    return render(request,"accounts/about.html")

def service_view(request):
    return render(request,"accounts/service.html")


