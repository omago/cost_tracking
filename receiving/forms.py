#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.utils import timezone

from .models import Receiving as Model


class ReceivingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReceivingForm, self).__init__(*args, **kwargs)
        self.fields["date_of_receiving"].widget.attrs.update({'class': 'date'})
        self.fields['received_by'].label_from_instance = lambda obj: "%s %s (%s)" % (obj.first_name, obj.last_name, obj.username)

    class Meta:
        model = Model
        exclude = ("deleted", "deleted_by", "deleted_datetime", "created_by", "creation_datetime")

    def save(self, commit=True, created_by=None):
        receiving = super(ReceivingForm, self).save(commit=False)
        if not receiving.pk:
            receiving.created_by = created_by
            receiving.creation_datetime = timezone.now()

        if commit:
            receiving.save()

        return receiving