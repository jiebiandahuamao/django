# -*- encoding:utf8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Put_Help(models.Model):
    user_id = models.CharField(max_length=5,default='000',verbose_name=u"id")
    what_put = models.CharField(max_length=255,default='',null=False,blank=False,verbose_name=u"提供what")
    time_zone = models.CharField(max_length=20,default='',null=False,blank=False,verbose_name=u"时间段")
    money = models.CharField(max_length=10,default='',null=False,blank=False)
    status = models.IntegerField(choices=((1,u'冻结'),(2,u'正常')),default=2,verbose_name=u"状态")
    note = models.CharField(max_length=50,default="",null=True,verbose_name=u"备注")
    add_time = models.DateTimeField()

    class Mete:

        verbose_name = u"提供帮助表"
        verbose_name_plural = verbose_name
