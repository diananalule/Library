from asyncio.windows_events import NULL
from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from system_user.models import CustomUser
from .models import Book
import datetime
from datetime import date

@login_required(login_url='/login')
def Books(request, user_id):
    context = {}
    context['books'] = ''
    user = CustomUser.objects.get(id=user_id)
    if user.role == "Admin":
        books = Book.objects.all()
        context['books'] = books
    else:
        books = Book.objects.filter(status="Available")
        context['books'] = books
    return render(request, "books.html", context)

@login_required(login_url='/login')
def searchBooks(request):
    context = {}
    user = request.user.role
    if request.method == "GET":
        value = request.GET.get("srch")
        if user == "Admin":
            books = Book.objects.filter(title__icontains=value)
            context['books'] = books
        else:
            books = Book.objects.filter(title__icontains=value)
            books=books.filter(status="Available")
            context['books'] = books

    return render(request, "books.html", context)

@login_required(login_url='/login')
def addbookurl(request):
    return render(request, "addbook.html")

@login_required(login_url='/login')
def addBook(request):
    user = request.user.id
    role = request.user.role
    if request.method == "GET":
        title = request.GET.get('title')
        author = request.GET.get('author')
        genre = request.GET.get('genre')
        status ="Available"
        book = Book(title=title,
        author=author,
        genre = genre,
        status=status,
        )
        if role == "Admin":
            book.save()
            return redirect("/catalog/" + str(user) )
    return redirect("/catalog/" + str(user) ) 

@login_required(login_url='/login')
def borrowBook(request, book_id):
    user = request.user.id
    try:
        book = Book.objects.get(id=book_id)
    except:
        book = None
    if book != None:
        new_user = CustomUser.objects.get(id=user)
        try:
            borrowed = Book.objects.get(borrower = new_user)
        except:
            borrowed = None
        book.status = "Borrowed"
        book.borrower = CustomUser.objects.get(id=user)
        book.return_date = datetime.datetime.now() + datetime.timedelta(days=7)
        if borrowed == None:
            book.save()
        return redirect("/catalog/" + str(user))
    return redirect("/catalog/" + str(user))

@login_required(login_url='/login')
def deleteBook(request, book_id):
    user = request.user.id
    if request.method == "GET":
        book = Book.objects.get(id=book_id)
        book.delete()
    return redirect("/catalog/" + str(user) )

@login_required(login_url='/login')
def returnBook(request, book_id):
    user = request.user.id
    if request.method == "GET":
        book = Book.objects.get(id = book_id)
        book.status = "Available"
        book.borrower = None
        book.save()
    return redirect("/catalog/" + str(user) )

@login_required(login_url='/login')
def notifications(request):
    user = request.user
    context = {}
    fine = "0"
    totalfine = 0
    now = datetime.datetime.now()
    try:
        book = Book.objects.get(borrower = user)
    except:
        book = None
    borrowed_books = Book.objects.filter(status = "Borrowed")
    for bk in borrowed_books:
        returndate = bk.return_date
        time = date(now.year, now.month, now.day) - date(returndate.year, returndate.month, returndate.day)
        print("Time: ",time)
        if (time.days >=1 and time.days < 10):
            totalfine += 5000
        elif (time.days >= 10):
            totalfine += 15000
    totalfine = "{:,}".format(totalfine)
    context["totalfine"] = totalfine
    if book != None:
        returndate = book.return_date
        time = date(now.year, now.month, now.day) - date(returndate.year, returndate.month, returndate.day)
        if (time.days >=1 and time.days < 10):
            fine = "5,000"
        elif (time.days >= 10):
            fine = "15,000"
        context["fine"] = fine
    return render(request, "notifications.html", context)








# Create your views here.
