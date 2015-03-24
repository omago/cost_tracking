#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import modelformset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum

from cost_tracking.settings.base import RESULTS_PER_PAGE

from core.helpers.view import get_delete

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

    order_by = request.GET.get("order_by")
    order_type = request.GET.get("order_type")
    rows_list = Model.objects.all()
    rows_list = rows_list.filter(deleted=None).annotate(total_sum=Sum('cost__amount'))


    if order_by:
        if order_type == "asc":
            order = order_by
        else:
            order = "-" + order_by
        rows_list = rows_list.order_by(order)

    paginator = Paginator(rows_list, RESULTS_PER_PAGE)
    page = request.GET.get('page')

    try:
        rows = paginator.page(page)
    except PageNotAnInteger:
        rows = paginator.page(1)
    except EmptyPage:
        rows = paginator.page(paginator.num_pages)

    context["rows"] = rows

    return render_to_response(context["template_path"] + "/list.html", context, context_instance=RequestContext(request))


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
            receipt_costs = Cost.objects.filter(receipt_id=pk).order_by("pk")
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
    context["pk"] = pk
    context["fields"] = model_form(instance=Model.objects.get(pk=pk))
    context["receipt_costs"] = Cost.objects.filter(receipt_id=pk).order_by("pk")

    return render_to_response("receipt/details.html", context, context_instance=RequestContext(request))

@login_required
def delete(request, pk):
    return get_delete(request, model, pk, "/receipt/")