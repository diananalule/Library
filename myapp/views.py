from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>home</h1>")
