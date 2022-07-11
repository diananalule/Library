#from django.forms import ModelForm
from random import choices
from telnetlib import STATUS
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    updated = forms.DateTimeField(auto_now_add=True)
    publication_date = forms.DateField()
    status = forms.CharField(max_length=30, choices=STATUS)
    subject_area = forms.CharField(max_length=100)