#-*- coding:utf8 -*-
"""djang_start URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
# from apps.users.views import user_login   #面向函数
from apps.users.views import LoginView,RegisterView,ActiveUserView


from message.views import get_message

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # url(r'^message/$', get_message,name = 'msg'),
    url(r'^$', TemplateView.as_view(template_name="main.html"),name='main'),
    # url(r'^login/$',user_login,name='login'),     #面向函数
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^reg/$', RegisterView.as_view(),name='reg'),
    url(r'^captcha/',include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name = "useractive")
]
