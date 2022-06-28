from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('/login', views.Login_view, name='Login_view'),
    path('', views.Logout_view, name='Logout_view'),
    path('', views.Register_view, name='Register_view')
]
