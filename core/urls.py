#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('core.views',
    url(r'^account/login/$', 'account.login'),
    url(r'^account/logout_user/$', 'account.logout_user'),

    url(r'^user/form/(?P<pk>.*)/', 'users.form'),
    url(r'^user/form/', 'users.form'),
    url(r'^user/details/(?P<pk>.*)/', 'users.details'),
    url(r'^user/delete/(?P<pk>.*)/', 'users.delete'),
    url(r'^user/list', 'users.list'),
    url(r'^user/', 'users.index'),

    url(r'^access-denied/$', 'default.access_denied'),
    url(r'^', 'default.index'),
)