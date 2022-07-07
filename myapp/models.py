from re import T
import re
from sre_constants import CATEGORY
from django.db import models
class Book(models.Model):
    STATUS = [
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('unavailable', 'Unavailable')  
    ]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=True)
    publication_date = models.DateField()
    status = models.CharField(max_length=30, choices=STATUS)
    subject_area = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'books' 

    def __str__(self):
        return self.title


class Borrower(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)
    return_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return self.name


class Payment(models.Model):
    CATEGORY = [
        ("cash", "Cash"),
        ("bank", "Bank"),
    ]
    amount_to_pay = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200)
    payment_date = models.DateTimeField(auto_now_add=True,null=True)