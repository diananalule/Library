from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Book
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def home(request):
    books = Book.objects.all()  # Gets all books

    context = {'books': books}
    return render(request, "accounts/index.html", context)


@login_required(login_url="/login/")
def showBook(request, pk):
    book = Book.objects.get(id=pk)

    context = {'book': book}
    return render(request, "accounts/show_book.html", context)
