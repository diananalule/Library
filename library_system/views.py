from django.shortcuts import render, redirect
from system_user.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password
from .forms import signupForm


def loginView(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        context["email"] = email
        context["password"] = password
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/books/" + str(user.id))
        else:
            messages.error(request, "Invalid email or password")
            return render(request, "login.html", context)
    return render(request, "login.html", context)


def signupView(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')
        sex = request.POST.get('sex')
        username = request.POST.get('username')
        context["name"] = name
        context["email"] = email
        context["confirm_password"] = confirm_password
        context["role"] = role
        context["sex"] = sex
        context["date_joined"] = datetime.now()
        context["username"] = username
        context["is_active"] = True
        context["password"] = password
        user = signupForm(context)

        if user.is_valid():
            if password == confirm_password:
                context["password"] = make_password(password)
                user = signupForm(context)
                user.save()
                messages.success(request, "User created successfully")
                return redirect('/login')
            else:
                messages.error(request, "Passwords do not match")
                return render(request, "signup.html", context)
        else:
            context["password"] = password
            messages.error(request, user.errors)
            return render(request, "signup.html", context)
    return render(request, "signup.html")


@login_required(login_url='/login/')
def logoutView(request):
    logout(request)
    return redirect("/login/")


@login_required(login_url='/login/')
def booksView(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    context = {"user": user}
    return render(request, "books.html", context)