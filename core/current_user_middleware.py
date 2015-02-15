#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db.models import signals
from django.utils.functional import curry

from core import field_registry

class CurrentUserMiddleware(object):
    def process_request(self, request):
        if request.method in ('GET', 'HEAD', 'OPTIONS', 'TRACE'):
            return

        if hasattr(request, 'user') and request.user.is_authenticated():
            user = request.user
        else:
            user = None

        update_users = curry(self.update_users, user)
        signals.pre_save.connect(update_users, dispatch_uid=request, weak=False)

    def update_users(self, user, sender, instance, **kwargs):
        registry = field_registry.FieldRegistry()
        if sender in registry:
            for field in registry.get_fields(sender):
                setattr(instance, field.name, user)

    def process_response(self, request, response):
        signals.pre_save.disconnect(dispatch_uid=request)
        return response