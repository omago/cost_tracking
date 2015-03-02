#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'core/static/'}),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^/*', include("receipt.urls")),
    url(r'^/*', include("receiving_category.urls")),
    url(r'^/*', include("receiving.urls")),
    url(r'^/*', include("cost_category.urls")),
    url(r'^/*', include("cost_subcategory.urls")),
    url(r'^/*', include("cost_name.urls")),
    url(r'^/*', include("cost.urls")),
    url(r'^/*', include("seller.urls")),
    url(r'^/*', include("cost.urls")),
    url(r'^/*', include("core.urls")),
)