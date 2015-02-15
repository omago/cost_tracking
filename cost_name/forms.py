#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import CostName as Model
from cost_subcategory.models import CostSubcategory


class CostNameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CostNameForm, self).__init__(*args, **kwargs)

        if args or kwargs:
            if args:
                cost_category = args[0].get("cost_category", None)
            else:
                cost_category = kwargs["instance"].cost_category

            self.fields['cost_subcategory'].queryset = CostSubcategory.objects.filter(cost_category=cost_category)
        else:
            self.fields['cost_subcategory'].queryset = CostSubcategory.objects.none()

    class Meta:
        model = Model