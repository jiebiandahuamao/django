# -*- coding:utf8 -*-
"""
author:cw
time:
"""

from django import forms
from simplemathcaptcha.fields import MathCaptchaField

class Regform(forms.Form):
    email = forms.CharField(required=True,max_length=20)
    password = forms.CharField(required=True,min_length=5)
    captcha = MathCaptchaField(error_messages={"invalid":u"验证码错误"})
