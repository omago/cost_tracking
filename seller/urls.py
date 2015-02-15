#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .settings import context

urlpatterns = patterns(context["app_folder"] + '.views',
    url(r'^' + context["url_main"] + '/form/(?P<pk>.*)/', 'form'),
    url(r'^' + context["url_main"] + '/form/', 'form'),
    url(r'^' + context["url_main"] + '/details/(?P<pk>.*)/', 'details'),
    url(r'^' + context["url_main"] + '/delete/(?P<pk>.*)/', 'delete'),
    url(r'^' + context["url_main"] + '/list', 'list'),
    url(r'^' + context["url_main"] + '/', 'list'),
)