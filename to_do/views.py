#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext

from core.helpers.view import get_details, get_form, get_delete
from cost_tracking.settings.base import RESULTS_PER_PAGE
from .settings import context
from .models import ToDo as Model
from .forms import ToDoForm as ModelForm

model = Model
model_form = ModelForm

@login_required
def list(request):

    order_by = request.GET.get("order_by")
    order_type = request.GET.get("order_type")
    rows_list = model.objects.all()

    rows_list = rows_list.filter(deleted=None).filter(finished=None)

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
    return get_form(request, model, model_form, pk, context, "common/form.html")


@login_required
def details(request, pk):
    return get_details(request, model, model_form, pk, context, "common/details.html")

@login_required
def delete(request, pk):
    return get_delete(request, model, pk, "/cost-category/")

@login_required
def finished(request, pk):
    referer = request.META.get('HTTP_REFERER')

    entry = model.objects.get(pk=pk)
    entry.finished = True
    entry.finished_datetime = timezone.now()
    entry.save()

    return HttpResponseRedirect(referer)