from django.contrib import admin
from myapp.models import Book
from myapp.models import Borrower
# Register your models here.
admin.site.register(Book)
admin.site.register(Borrower)
