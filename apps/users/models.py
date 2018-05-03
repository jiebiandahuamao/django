# -*- encoding:utf8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    user_id = models.CharField(max_length=5,default='000',verbose_name=u'id')
    nick_name = models.CharField(max_length=50,verbose_name=u"昵称",default=u"")
    birday = models.DateField(verbose_name=u"生日",null=True,blank=True)
    gender = models.CharField(max_length=10, choices=(("male",u"男"),("female",u"女")),default="female")
    address = models.CharField(max_length=100,default=u"")
    mobile = models.CharField(max_length=11,null=False,blank=False)
    image = models.ImageField(upload_to="image/%Y/%m",default=u'image/default.png',max_length=100)

    class Meta:

        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type = models.CharField(choices=(("register",u"注册"),('forget',u"找回密码")),max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name