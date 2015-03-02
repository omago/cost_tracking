#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.utils import timezone

from .models import Receipt as Model


class ReceiptForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReceiptForm, self).__init__(*args, **kwargs)

        self.fields["date_of_receipt"].widget.attrs.update({'class': 'date'})
        self.fields['paid_by'].label_from_instance = lambda obj: "%s %s (%s)" % (obj.first_name, obj.last_name, obj.username)

    class Meta:
        model = Model
        fields = ("paid_by",
                  "date_of_receipt",
                  "seller",
                  "attachment",
                  "description")

    def save(self, commit=True, created_by=None, *args, **kwargs):

        receipt = super(ReceiptForm, self).save(commit=False)

        if not receipt.pk:
            receipt.created_by = created_by
            receipt.creation_datetime = timezone.now()

        if commit:
            receipt.save()

        return receipt