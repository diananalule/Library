#from django.forms import ModelForm
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    updated = forms.DateTimeField(auto_now_add=True)
    publication_date = forms.DateField()
    status = forms.CharField()
    subject_area = forms.CharField()
    
    class Meta:
        model = Book
        fields = [
            'title','author','publlication_date','status','subject_area'
        ]