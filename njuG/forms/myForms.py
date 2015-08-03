# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True)
    password = forms.CharField(max_length=254, required=True)

class ProfileForm(forms.Form):
    nickName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder':'昵称','required':'true'}),
                               required=True, error_messages={'required': '请填写昵称'})
    school = forms.ChoiceField(settings.SCHOOL_LIST, initial = u'南京大学')
    degree = forms.ChoiceField(((u'本科',u'本科'), (u'硕士',u'硕士'), (u'博士', u'博士')), initial = '本科')
    role = forms.ChoiceField(((u'攻',u'攻'), (u'受',u'受'), (u'不限',u'不限'), (u'保密', u'保密')), initial = 4)
    
    BIRTH_YEAR_CHOICES = [(i,i) for i in range(1970,2005)]
    birth_year = forms.ChoiceField(BIRTH_YEAR_CHOICES, initial=1995)
    
class BlogForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'标题','required':'true'}), 
                            required=True, error_messages={'required': '请填写标题'})
    blogContent = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'内容','required':'true'}),required=True)
    isAnonymous = forms.BooleanField(initial=False, required=False)
    
class ActivityForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'找自习小伙伴 打球 爬山等','required':'true'}), 
                            required=True, error_messages={'required': '请填写名称'})
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'时间、地点等','required':'true'}),required=True)
    onlyForSchool = forms.BooleanField(initial=True, required=False)
    openToAll = forms.BooleanField(initial=True, required=False)
    contact = forms.ChoiceField([(u'私信我',u'私信我'),(u'微信',u'微信')], initial=u'私信我', required=False)
    detailContact = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder':'填写微信号'}), 
                            required=False, error_messages={'required': '请填写微信号'})
    openSchoolList = forms.MultipleChoiceField(settings.SCHOOL_LIST,initial=[u'南京大学'],required=False)