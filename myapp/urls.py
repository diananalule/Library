from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.about_view, name="about_view"),
    path("service/", views.service_view, name="service_view"),

]
