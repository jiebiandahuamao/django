# -*- coding:utf8 -*-
"""
author:cw
time:
"""
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True,max_length=20)
    password = forms.CharField(required=True,min_length=5)
