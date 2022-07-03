from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
#from . import views
# Creating the views here.


def Login_view(request):
    if request.user.is_authenticated:
        return render(request,"accounts/already-logged-in.html",{})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Inavalid username or password"}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        return redirect("/")
        print(username, password)
    return render(request, 'accounts/login.html', {})


def Logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    return render(request, 'accounts/logout_view.html', {})


def Register_view(request):
    return render(request, 'accounts/register_view.html', {})
