#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author LiuAo
    @Date 2022/9/9 15:11
    @Describe 
    @Version 1.0
"""
from django.urls import re_path as url
from  jobs import views

urlpatterns = [
    #职位列表
    url(r"^joblist/",views.joblist,name="joblist"),
    url(r"^job/(?P<job_id>\d+)/$", views.detail,name='detail')
]