#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.utils import timezone
from django.forms import TextInput

from .models import Receiving as Model


class ReceivingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReceivingForm, self).__init__(*args, **kwargs)
        self.fields["date_of_receiving"].widget.attrs.update({'class': 'date'})
        self.fields['received_by'].label_from_instance = lambda obj: "%s %s (%s)" % (obj.first_name, obj.last_name, obj.username)

        self.fields["description"].widget = TextInput()

        self.initial["date_of_receiving"] = timezone.now()
        #self.initial["received_by"] = user

    class Meta:
        model = Model
        fields = ("receiving_category", "amount", "description", "received_by", "date_of_receiving")

    def save(self, commit=True, created_by=None):
        receiving = super(ReceivingForm, self).save(commit=False)
        if not receiving.pk:
            receiving.created_by = created_by
            receiving.creation_datetime = timezone.now()

        if commit:
            receiving.save()

        return receiving