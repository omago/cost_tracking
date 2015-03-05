#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cost_tracking',            # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'omago',
        'PASSWORD': 'omago.123',
        'HOST': '127.0.0.1',           # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

INTERNAL_IPS = ('127.0.0.1',)

# DEBUG_TOOLBAR_PANELS = (
#     'debug_toolbar.panels.version.VersionPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request_vars.RequestPanel',
#     'debug_toolbar.panels.template.TemplatePanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.signals.SignalPanel',
#     'debug_toolbar.panels.logger.LoggingPanel',
# )