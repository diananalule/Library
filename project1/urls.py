"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import (
    Login_view,
    Logout_view,
    Register_view,

)
from myapp.views import(book_create_view, home, about_view,  service_view, showBook)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include("myapp.urls")),
    path('accounts/', include("accounts.urls")),
    path('login/', Login_view),
    path('logout/', Logout_view),
    path('register/', Register_view),
    path('', home),
    path('about/', about_view),
    path("service/", service_view),
    path('show-book/<str:pk>/', showBook, name='showbook'),
    path("book/",book_create_view),

]
