from django.forms import ModelForm
from django import forms
from .models import Books


class BooksForm(ModelForm):
    title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=True)
    Publication_date = models.DateField()
    Subject_area = models.CharField(max_length=100)