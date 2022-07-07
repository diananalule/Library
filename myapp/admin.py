from django.contrib import admin
from myapp.models import Book
from myapp.models import Borrower
from myapp.models import Payment
# Register your models here.
admin.site.register(Book)
admin.site.register(Borrower)
admin.site.register(Payment)
