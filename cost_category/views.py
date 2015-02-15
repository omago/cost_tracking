#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from core.helpers.view import get_list, get_details, get_form, get_delete
from .settings import context
from .models import CostCategory as Model
from .forms import CostCategoryForm as ModelForm

model = Model
model_form = ModelForm

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
    return get_delete(request, model, pk, "/cost-category/")