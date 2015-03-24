#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse

from core.helpers.view import get_list, get_details, get_form, get_delete
from .settings import context
from .models import CostName as Model
from .forms import CostNameForm as ModelForm

model = Model
model_form = ModelForm


@login_required
def autocomplete(request):
    if request.is_ajax():
        cost_name = request.GET.get("cost_name")
        cost_category = request.GET.get("cost_category")
        cost_subcategory = request.GET.get("cost_subcategory")

        cost_names = Model.objects.filter(name__istartswith=cost_name).exclude(deleted=True)

        if cost_category:
            cost_names = cost_names.filter(cost_category_id=cost_category)

        if cost_subcategory:
            cost_names = cost_names.filter(cost_subcategory_id=cost_subcategory)

        data = serializers.serialize("json", cost_names)

        return HttpResponse(data, content_type='application/json')

    return HttpResponse("")


@login_required
def list(request):
    return get_list(request, model, context, context["template_path"] + "/list.html", hide_deleted=True)


@login_required
def form(request, pk=None):
    return get_form(request, model, model_form, pk, context, "common/form.html")


@login_required
def details(request, pk):
    return get_details(request, model, model_form, pk, context, "common/details.html")

@login_required
def delete(request, pk):
    return get_delete(request, model, pk, "/cost-name/")