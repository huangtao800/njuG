# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True)
    password = forms.CharField(max_length=254, required=True)

class ProfileForm(forms.Form):
    nickName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder':'昵称','required':'true'}),
                               required=True, error_messages={'required': '请填写昵称'})
    school = forms.ChoiceField(((1,'南京大学'), (2,'其他学校')), initial = 1)
    degree = forms.ChoiceField(((1,'本科'), (2,'硕士'), (3, '博士')), initial = 1)
    role = forms.ChoiceField(((1,'攻'), (2,'受'), (3,'不限'), (4, '-')), initial = 4)
    
class BlogForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'标题','required':'true'}), 
                            required=True, error_messages={'required': '请填写标题'})
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'内容','required':'true'}),required=True)
    isAnonymous = forms.BooleanField(initial=False, required=False)