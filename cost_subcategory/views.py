#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse

from core.helpers.view import get_list, get_details, get_form, get_delete
from .settings import context
from .models import CostSubcategory as Model
from .forms import CostSubcategoryForm as ModelForm

model = Model
model_form = ModelForm


@login_required
def get_json_list(request):
    if request.is_ajax():
        category_id = request.GET.get("category_id", None)
        print category_id
        if not category_id:
            category_id = request.GET.getlist("category_id[]", None)
            subcategories = Model.objects.filter(cost_category_id__in=category_id)
        else:
            subcategories = Model.objects.filter(cost_category_id=category_id)

        data = serializers.serialize("json", subcategories)

        return HttpResponse(data, content_type='application/json')

    return HttpResponse("")


@login_required
def list(request):
    return get_list(request, model, context, context["template_path"] + "/list.html")


@login_required
def form(request, pk=None):
    return get_form(request, model, model_form, pk, context, "common/form.html")


@login_required
def details(request, pk):
    return get_details(request, model, model_form, pk, context, "common/details.html")

@login_required
def delete(request, pk):
    return get_delete(request, model, pk, "/cost-subcategory/")