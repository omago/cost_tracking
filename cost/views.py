#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Sum

from core.helpers.view import get_list, get_details, get_form, get_delete

from .settings import context
from .models import Cost as Model
from .forms import CostForm as ModelForm
from .forms import CostSearchForm

model = Model
model_form = ModelForm


@login_required
def list(request):
    return get_list(request, model, context, context["template_path"] + "/list.html", hide_deleted=True)

@login_required
def form(request, pk=None):
    return get_form(request, model, model_form, pk, context, "common/form.html", True, True)

@login_required
def details(request, pk):
    return get_details(request, model, model_form, pk, context, "common/details.html")

@login_required
def delete(request, pk):
    return get_delete(request, model, pk, "/cost/")

@login_required
def report(request):
    context["search_form"] = CostSearchForm(request.GET)

    order_by = request.GET.get("order_by", None)
    order_type = request.GET.get("order_type", None)

    year = request.GET.get("year", None)
    month = request.GET.get("month", None)
    amount_from = request.GET.get("amount_from", None)
    amount_to = request.GET.get("amount_to", None)
    paid_by = request.GET.get("paid_by", None)
    cost_category_multiple = request.GET.getlist("cost_category_multiple", None)

    rows_list = Model.objects.all()

    if year:
        rows_list = rows_list.filter(date_of_cost__year=year)

    if month:
        rows_list = rows_list.filter(date_of_cost__month=month)

    if amount_from:
        rows_list = rows_list.filter(amount__gte=amount_from)

    if amount_to:
        rows_list = rows_list.filter(amount__lte=amount_to)

    if paid_by:
        rows_list = rows_list.filter(paid_by_id=paid_by)

    if cost_category_multiple:
        rows_list = rows_list.filter(cost_category__in=cost_category_multiple)

    rows_list = rows_list.filter(deleted=None)

    if order_by:
        if order_type == "asc":
            order = order_by
        else:
            order = "-" + order_by
        rows_list = rows_list.order_by(order)

    if request.GET:
        context["report_requested"] = True

    if len(request.GET) > 0:
        context["rows"] = rows_list
        context["sum"] = rows_list.aggregate(Sum("amount"))["amount__sum"]

    return render_to_response(context["template_path"] + "/report.html", context, context_instance=RequestContext(request))