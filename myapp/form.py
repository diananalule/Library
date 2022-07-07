from django.forms import ModelForm
from django import forms

class BorrowerForm(forms.Form):
    name = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=200)
    email= forms.CharField(max_length=200,null=True)
    return_date = forms.DateTimeField(auto_now_add=True)
    due_date = forms.DateField()