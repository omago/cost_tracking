#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm, Form
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.forms.models import BaseModelFormSet

from cost_category.models import CostCategory
from cost_subcategory.models import CostSubcategory
from cost_name.models import CostName
from .models import Cost as Model


class CostForm(ModelForm):
    cost_name_autocomplete = forms.CharField(max_length=1024, required=False, label="Naziv troška")

    def __init__(self, *args, **kwargs):
        super(CostForm, self).__init__(*args, **kwargs)

        self.fields["date_of_cost"].widget.attrs.update({'class': 'date'})
        self.fields['paid_by'].label_from_instance = lambda obj: "%s %s (%s)" % (obj.first_name, obj.last_name, obj.username)

        if args or kwargs:
            if args:
                cost_category = args[0].get("cost_category", None)
            else:
                cost_category = kwargs["instance"].cost_category

            self.fields['cost_subcategory'].queryset = CostSubcategory.objects.filter(cost_category=cost_category)
        else:
            self.fields['cost_subcategory'].queryset = CostSubcategory.objects.none()

        self.fields["cost_name"].widget = forms.HiddenInput()
        self.fields["cost_name_autocomplete"].widget.attrs["autocomplete"] = "off"
        self.fields["cost_name_autocomplete"].widget.attrs["class"] = "autocomplete"
        self.fields["cost_name_autocomplete"].widget.attrs["rel"] = "/cost-name/autocomplete/"

        if kwargs:
            self.fields["cost_name_autocomplete"].initial = kwargs["instance"].cost_name

    class Meta:
        model = Model
        fields = ("cost_category",
                  "cost_subcategory",
                  "cost_name",
                  "cost_name_autocomplete",
                  "quantity",
                  "amount",
                  "paid_by",
                  "date_of_cost",
                  "seller",
                  "attachment",
                  "description")

    def save(self, commit=True, created_by=None, *args, **kwargs):

        cost = super(CostForm, self).save(commit=False)

        cost_name_autocomplete = self.cleaned_data["cost_name_autocomplete"]
        try:
            cost_name = CostName.objects.filter(cost_category=cost.cost_category)
            if cost.cost_subcategory:
                cost_name = cost_name.filter(cost_subcategory=cost.cost_subcategory)
            cost_name = cost_name.get(name=cost_name_autocomplete)
        except CostName.DoesNotExist:
            cost_name = CostName()
            cost_name.cost_category = cost.cost_category
            cost_name.cost_subcategory = cost.cost_subcategory
            cost_name.name = cost_name_autocomplete
            cost_name.save()

        cost.cost_name = cost_name

        if not cost.pk:
            cost.created_by = created_by
            cost.creation_datetime = timezone.now()

        if commit:
            cost.save()

        return cost


class BaseCostFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseCostFormSet, self).__init__(*args, **kwargs)


class CostFormsetForm(ModelForm):
    cost_name_autocomplete = forms.CharField(max_length=1024, required=False, label="Naziv troška")

    def __init__(self, *args, **kwargs):
        super(CostFormsetForm, self).__init__(*args, **kwargs)

        self.fields["cost_category"].widget.attrs["class"] = "cost_category_select"
        self.fields["cost_subcategory"].widget.attrs["class"] = "cost_subcategory_select"
        self.fields["amount"].widget.attrs["placeholder"] = "Iznos"
        self.fields["quantity"].widget.attrs["placeholder"] = "Količina"
        self.fields['quantity'].required = False
        self.fields["description"].widget = forms.TextInput()
        self.fields["description"].widget.attrs["placeholder"] = "Opis"
        self.fields["cost_name"].widget = forms.HiddenInput()
        self.fields["cost_name_autocomplete"].widget.attrs["autocomplete"] = "off"
        self.fields["cost_name_autocomplete"].widget.attrs["placeholder"] = "Naziv proizvoda"
        self.fields["cost_name_autocomplete"].widget.attrs["class"] = "autocomplete cost-name"
        self.fields["cost_name_autocomplete"].widget.attrs["rel"] = "/cost-name/autocomplete/"

        prefix = kwargs["prefix"]

        if "data" in kwargs and prefix + "-cost_category" in kwargs["data"]:
            cost_category_id = kwargs["data"][prefix + "-cost_category"]
            if len(cost_category_id) > 0:
                self.fields['cost_subcategory'].queryset = CostSubcategory.objects\
                    .filter(cost_category_id=int(cost_category_id))
        elif "instance" in kwargs:
            cost_category = kwargs["instance"].cost_category
            self.fields['cost_subcategory'].queryset = CostSubcategory.objects.filter(cost_category=cost_category)
            self.fields["cost_name_autocomplete"].initial = kwargs["instance"].cost_name
        else:
            self.fields['cost_subcategory'].queryset = CostSubcategory.objects.none()

    class Meta:
        model = Model
        fields = ("cost_category",
                  "cost_subcategory",
                  "cost_name",
                  "cost_name_autocomplete",
                  "amount",
                  "quantity",
                  "description")

    def save(self, commit=True, created_by=None, receipt=None, *args, **kwargs):
        cost = super(CostFormsetForm, self).save(commit=False)

        if "cost_name_autocomplete" in self.cleaned_data:
            cost_name_autocomplete = self.cleaned_data["cost_name_autocomplete"]
            try:
                cost_name = CostName.objects.filter(cost_category=cost.cost_category)
                if cost.cost_subcategory:
                    cost_name = cost_name.filter(cost_subcategory=cost.cost_subcategory)
                cost_name = cost_name.get(name=cost_name_autocomplete)
            except CostName.DoesNotExist:
                cost_name = CostName()
                cost_name.cost_category = cost.cost_category
                cost_name.cost_subcategory = cost.cost_subcategory
                cost_name.name = cost_name_autocomplete
                cost_name.save()

            if not cost.quantity:
                cost.quantity = 1

            cost.cost_name = cost_name
            cost.receipt = receipt
            cost.paid_by = receipt.paid_by
            cost.date_of_cost = receipt.date_of_receipt
            cost.seller = receipt.seller

            if not cost.pk:
                cost.created_by = created_by
                cost.creation_datetime = timezone.now()

            if commit:
                cost.save()

        return cost


class CostSearchForm(Form):

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

    choices = [("", "--------")]

    for i in range(1, 32):
        choices.append((str(i), str(i)))

    day = forms.ChoiceField(choices=choices, label="Dan", required=False)

    amount_from = forms.DecimalField(label="Iznos od", required=False)
    amount_to = forms.DecimalField(label="Iznos do", required=False)

    cost_category_multiple = forms.ModelMultipleChoiceField(queryset=CostCategory.objects.all(), label="Kategorija troška", required=False)
    cost_subcategory_multiple = forms.ModelMultipleChoiceField(queryset=CostSubcategory.objects.all(), label="Podkategorija troška", required=False)

    paid_by = forms.ModelChoiceField(queryset=User.objects.all(), label="Platio", required=False)


    def __init__(self, *args, **kwargs):
        super(CostSearchForm, self).__init__(*args, **kwargs)

        self.fields["cost_category_multiple"].widget.attrs["size"] = "10"
        self.fields["cost_subcategory_multiple"].widget.attrs["size"] = "8"

        if args or kwargs:
            if args:
                cost_category = args[0].getlist("cost_category_multiple", None)
            else:
                cost_category = kwargs["instance"].cost_category

            self.fields['cost_subcategory_multiple'].queryset = CostSubcategory.objects.filter(cost_category__in=cost_category)
        else:
            self.fields['cost_subcategory_multiple'].queryset = CostSubcategory.objects.none()