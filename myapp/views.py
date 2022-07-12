from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from myapp.form import BookForm
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
    print (request.POST)
    
    form=BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookForm()
    context = { "form": form}
    return render(request,"accounts/book.html",context)
