#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Seller as Model


class SellerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SellerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Model