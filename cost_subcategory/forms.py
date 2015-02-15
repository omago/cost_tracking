#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import CostSubcategory as Model


class CostSubcategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CostSubcategoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Model