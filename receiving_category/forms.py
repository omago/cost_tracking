#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import ReceivingCategory as Model


class ReceivingCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReceivingCategoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Model