#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm, Form
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User

from cost_category.models import CostCategory
from .models import Cost as Model
from django.forms import TextInput


class CostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)
        super(CostForm, self).__init__(*args, **kwargs)

        self.fields["date_of_cost"].widget.attrs.update({'class': 'date'})
        self.fields['paid_by'].label_from_instance = lambda obj: "%s %s (%s)" % (obj.first_name, obj.last_name, obj.username)

        self.fields["description"].widget = TextInput()

        self.initial["cost_category"] = CostCategory.objects.get(pk=1)
        self.initial["date_of_cost"] = timezone.now()
        self.initial["paid_by"] = user

    class Meta:
        model = Model
        fields = ("cost_category",
                  "amount",
                  "description",
                  "paid_by",
                  "date_of_cost")

    def save(self, commit=True, created_by=None, *args, **kwargs):
        cost = super(CostForm, self).save(commit=False)

        if not cost.pk:
            cost.created_by = created_by
            cost.creation_datetime = timezone.now()

        if commit:
            cost.save()

        return cost


class CostSearchForm(Form):

    choices = [("", "--------")]

    for i in range(2017, timezone.now().year + 1):
        choices.append((str(i), str(i)))

    year = forms.ChoiceField(choices=choices, label="Godina", required=False)

    month = forms.ChoiceField(choices=(
        ("", "--------"),
        ("1", "Siječanj"),
        ("2", "Veljača"),
        ("3", "Ožujak"),
        ("4", "Travanj"),
        ("5", "Svibanj"),
        ("6", "Lipanj"),
        ("7", "Srpanj"),
        ("8", "Kolovoz"),
        ("9", "Rujan"),
        ("10", "Listopad"),
        ("11", "Studeni"),
        ("12", "Prosinac")
    ), label="Mjesec", required=False)

    amount_from = forms.DecimalField(label="Iznos od", required=False)
    amount_to = forms.DecimalField(label="Iznos do", required=False)

    cost_category_multiple = forms.ModelMultipleChoiceField(queryset=CostCategory.objects.all(), label="Kategorija troška", required=False)

    paid_by = forms.ModelChoiceField(queryset=User.objects.all(), label="Platio", required=False)

    def __init__(self, *args, **kwargs):
        super(CostSearchForm, self).__init__(*args, **kwargs)

        self.fields["cost_category_multiple"].widget.attrs["size"] = "10"

