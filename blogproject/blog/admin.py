# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post,Category,Tag
import sys
reload(sys)
sys.setdefaultencoding("utf8")
class Postadmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author'] #在post界面显示更多信息
admin.site.register(Post,Postadmin)
admin.site.register(Tag)
admin.site.register(Category)
# Register your models here.
