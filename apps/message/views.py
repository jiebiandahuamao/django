#-*- coding:utf8 -*-
from django.shortcuts import render

# Create your views here.

def get_message(request):

    return render(request, 'message/message.html')