#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required

from core.helpers.view import get_list, get_details, get_form, get_delete
from .settings import context
from .models import Receiving as Model
from .forms import ReceivingForm as ModelForm

model = Model
model_form = ModelForm

@login_required
def list(request):
    return get_list(request, model, context, context["template_path"] + "/list.html", hide_deleted=True)


@login_required
def form(request, pk=None):
    return get_form(request, model, model_form, pk, context, "common/form.html", True, False, True)


@login_required
def details(request, pk):
    return get_details(request, model, model_form, pk, context, "common/details.html")

@login_required
def delete(request, pk):
    return get_delete(request, model, pk, "/receiving/")