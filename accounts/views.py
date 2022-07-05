from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

#from . import views
# Creating the views here.


def Login_view(request):
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
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    context = {"form":form}
    return render(request, 'accounts/register.html',{"form":form})
