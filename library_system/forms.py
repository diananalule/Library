from django.forms import ModelForm
from system_user.models import CustomUser
from django import forms
from django.contrib.auth.hashers import check_password
import re


class signupForm(ModelForm):

    class Meta():
        model = CustomUser
        fields = '__all__'