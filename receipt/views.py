#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import modelformset_factory

from core.helpers.view import get_list, get_details, get_delete

from .settings import context
from .models import Receipt as Model
from .forms import ReceiptForm as ModelForm
from cost.forms import CostFormsetForm
from cost.forms import BaseCostFormSet
from cost.models import Cost

model = Model
model_form = ModelForm


@login_required
def list(request):
    return get_list(request, model, context, context["template_path"] + "/list.html", hide_deleted=True)

@login_required
def form(request, pk=None):
    number_of_fields = 20
    CostFormset = modelformset_factory(Cost, form=CostFormsetForm, formset=BaseCostFormSet, extra=number_of_fields)

    if request.POST:
        if pk:
            entry = Model.objects.get(pk=pk)
            form = ModelForm(request.POST, instance=entry)
            cost_formset = CostFormset(request.POST)

        else:
            form = ModelForm(request.POST)
            cost_formset = CostFormset(request.POST)

        if form.is_valid() and cost_formset.is_valid():
            receipt = form.save(created_by=request.user)
            for cost_form in cost_formset:
                cost_form.save(created_by=request.user, receipt=receipt)

            return HttpResponseRedirect("/" + context["url_main"] + "/list/")
    else:
        if pk:
            form = ModelForm(instance=Model.objects.get(pk=pk))
            receipt_costs = Cost.objects.filter(receipt_id=pk)
            cost_formset = CostFormset(queryset=receipt_costs)
            cost_formset.extra = number_of_fields - len(receipt_costs)
        else:
            form = ModelForm()
            cost_formset = CostFormset(queryset=Cost.objects.none())

    context.update(csrf(request))
    context['form'] = form
    context['cost_formset'] = cost_formset

    return render_to_response("receipt/form.html", context, context_instance=RequestContext(request))

@login_required
def details(request, pk):
    return get_details(request, model, model_form, pk, context, "common/details.html")

@login_required
def delete(request, pk):
    return get_delete(request, model, pk, "/receipt/")