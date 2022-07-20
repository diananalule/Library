from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book

admin.site.register(Book)

# Register your models here.
