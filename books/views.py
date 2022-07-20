from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from system_user.models import CustomUser
from .models import Book

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
            books = Book.objects.filter(title__icontains=value) | Book.objects.filter(author__icontains=value) | Book.objects.filter(genre__icontains=value)
            context['books'] = books
        else:
            books = Book.objects.filter(title__icontains=value) | Book.objects.filter(author__icontains=value) | Book.objects.filter(genre__icontains=value)
            books=books.filter(status="Available")
            context['books'] = books

    return render(request, "books.html", context)

@login_required(login_url='/login')
def addbookurl(request):
    return render(request, "addbook.html")

@login_required(login_url='/login')
def addBook(request):
    user = request.user.id
    role = CustomUser.objects.get(id=user)
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
    print("Book: ", book_id)
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
        if borrowed == None:
            book.save()
        return redirect("/catalog/" + str(user))
    return redirect("/catalog/" + str(user))




# Create your views here.
