#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.utils import timezone

from .models import Receipt as Model
from seller.models import Seller


class ReceiptForm(forms.ModelForm):
    seller_autocomplete = forms.CharField(max_length=1024, required=False, label="Prodavatelj")

    def __init__(self, *args, **kwargs):
        super(ReceiptForm, self).__init__(*args, **kwargs)

        self.fields["description"].widget = forms.TextInput()
        self.fields["date_of_receipt"].widget.attrs.update({'class': 'date'})
        self.fields['paid_by'].label_from_instance = lambda obj: "%s %s (%s)" % (obj.first_name, obj.last_name, obj.username)
        self.fields["seller"].widget = forms.HiddenInput()
        self.fields["seller_autocomplete"].widget.attrs["autocomplete"] = "off"
        self.fields["seller_autocomplete"].widget.attrs["class"] = "autocomplete"
        self.fields["seller_autocomplete"].widget.attrs["rel"] = "/seller/autocomplete/"

        if "instance" in kwargs:
            self.fields["seller_autocomplete"].initial = kwargs["instance"].seller

    class Meta:
        model = Model
        fields = ("paid_by",
                  "date_of_receipt",
                  "seller",
                  "seller_autocomplete",
                  "attachment",
                  "description")

    def save(self, commit=True, created_by=None, *args, **kwargs):
        receipt = super(ReceiptForm, self).save(commit=False)

        if "seller_autocomplete" in self.cleaned_data:
            seller_autocomplete = self.cleaned_data["seller_autocomplete"]
            try:
                seller = Seller.objects.get(name=seller_autocomplete)
            except Seller.DoesNotExist:
                seller = Seller()
                seller.name = seller_autocomplete
                seller.save()

            receipt.seller = seller

        if not receipt.pk:
            receipt.created_by = created_by
            receipt.creation_datetime = timezone.now()

        if commit:
            receipt.save()

        return receipt