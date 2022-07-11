from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Book
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def home(request):
    books = Book.objects.all()  # gets all books
    context = {'books': books}
    return render(request, "accounts/index.html", context)


def about_view(request):
    return render(request, "accounts/about.html")


def service_view(request):
    return render(request, "accounts/service.html")

def book_create_view(request):
    context ={}
    return render(request,"accounts/book.html",context)
