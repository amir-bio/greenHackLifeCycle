# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 14:46:16 2018

@author: huika
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]