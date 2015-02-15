#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from core import field_registry

class CurrentUserField(models.ForeignKey):
    def __init__(self, **kwargs):
        super(CurrentUserField, self).__init__(User, **kwargs)

    def contribute_to_class(self, cls, name):
        super(CurrentUserField, self).contribute_to_class(cls, name)
        registry = field_registry.FieldRegistry()
        registry.add_field(cls, self)


class CommonFieldsManager(models.Manager):
    def not_deleted(self):
        return self.filter(deleted = None)


class CommonFields(models.Model):

    created = models.DateTimeField(editable=False, auto_now_add=True)
    created_by = CurrentUserField(related_name="+", editable=False)
    modified = models.DateTimeField(editable=False, auto_now=True)
    modified_by = CurrentUserField(related_name="+", editable=False)
    deleted = models.DateTimeField(editable=False, null=True)
    deleted_by = models.ForeignKey(User, related_name="+", editable=False, null=True)
    objects = CommonFieldsManager()

    class Meta:
        abstract = True


from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^core\.models\.common_fields\.CurrentUserField"])