from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('',views.Login_view, name='login'),
   path('',views.Logout_view, name='logout'),
   path('',views.Register_view, name='register')
]




