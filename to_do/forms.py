#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.utils import timezone

from .models import ToDo as Model


class ToDoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)
        super(ToDoForm, self).__init__(*args, **kwargs)

        self.fields['assignee'].label_from_instance = lambda obj: "%s %s (%s)" % (obj.first_name, obj.last_name, obj.username)
        self.fields["date_to"].widget.attrs.update({'class': 'date'})
        self.initial["assignee"] = user

    class Meta:
        model = Model
        exclude = ("finished",
                   "finished_datetime",
                   "created_by",
                   "creation_datetime",
                   "deleted",
                   "deleted_by",
                   "deleted_datetime")

    def save(self, commit=True, created_by=None, *args, **kwargs):
        to_do = super(ToDoForm, self).save(commit=False)

        if not to_do.pk:
            to_do.created_by = created_by
            to_do.creation_datetime = timezone.now()

        if commit:
            to_do.save()

        return to_do