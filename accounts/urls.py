from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('',views.Login_view, name='login'),
   path('logout_view',views.Logout_view, name='logout_view'),
   path('register_view',views.Register_view, name='register_view')
]




