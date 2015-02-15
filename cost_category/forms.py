#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import CostCategory as Model


class CostCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CostCategoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Model