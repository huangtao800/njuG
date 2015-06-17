# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True)
    password = forms.CharField(max_length=254, required=True)

class ProfileForm(forms.Form):
    school = forms.CharField(max_length=100,initial="南京大学")
    degree = forms.ChoiceField((1,'本科'),(2,'研究生'), initial = 1)
    
    
    