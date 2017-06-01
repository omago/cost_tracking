#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.utils import timezone

from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf

from cost_tracking.settings.base import RESULTS_PER_PAGE
from django.db.models import Q
from django.db.models import AutoField, CharField, TextField


def get_list(request, model_object, context, template, hide_deleted=False):
    order_by = request.GET.get("order_by")
    order_type = request.GET.get("order_type")
    rows_list = model_object.objects.all()
    search_term = request.GET.get("q")

    if hide_deleted is True:
        rows_list = rows_list.filter(deleted=None)

    if search_term:
        query = None
        for field in model_object._meta.fields:
            field_type = type(field)
            field_name = field.name
            if field_type is not AutoField and \
                            field_name != "created" and \
                            field_name != "created_by" and \
                            field_name != "deleted" and \
                            field_name != "deleted_datetime" and \
                            field_name != "deleted_by":
                q = None
                if field_name is "travel_worksheet_registration_number" and (field_type is CharField or
                                                                             field_type is TextField):
                    q = Q(**{"%s__contains" % field_name: search_term})

                if q:
                    if query:
                        query = query | q
                    else:
                        query = q

        rows_list = rows_list.filter(query)

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

    return render_to_response(template, context, context_instance=RequestContext(request))


def get_form(request, model_object, model_form, pk, context, template, created_by=False, file_upload=False, current_user=False):
    if request.POST:
        if pk:
            entry = model_object.objects.get(pk=pk)
            if file_upload:
                form = model_form(request.POST, request.FILES, instance=entry)
            else:
                form = model_form(request.POST, instance=entry)
        else:
            if file_upload:
                form = model_form(request.POST, request.FILES)
            else:
                form = model_form(request.POST)

        if form.is_valid():
            if created_by:
                form.save(created_by=request.user)
            else:
                form.save()
            return HttpResponseRedirect("/" + context["url_main"] + "/list/")
    else:
        if pk:
            entry = model_object.objects.get(pk=pk)
            form = model_form(instance=entry)
        else:
            if current_user:
                form = model_form(current_user=request.user)
            else:
                form = model_form()

    context.update(csrf(request))
    context['form'] = form

    return render_to_response(template, context, context_instance=RequestContext(request))


def get_details(request, model_object, model_form, pk, context, template):
    context["pk"] = pk
    context["fields"] = model_form(instance=model_object.objects.get(pk=pk))
    return render_to_response(template, context, context_instance=RequestContext(request))


def get_delete(request, model_object, pk, return_link):
    entry = model_object.objects.get(pk=pk)
    entry.deleted = True
    entry.deleted_datetime = timezone.now()
    entry.deleted_by = request.user
    entry.save()

    return HttpResponseRedirect(return_link)