#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from core.forms.user import UserForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cost_tracking.settings.base import RESULTS_PER_PAGE

context = {'page_title': "Korisnici"}

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='/access-denied/')
def index(request):
    return HttpResponseRedirect('/user/list/')


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='/access-denied/')
def list(request):
    rows_list = User.objects.all().order_by("-pk")
    paginator = Paginator(rows_list, RESULTS_PER_PAGE)
    page = request.GET.get('page')

    try:
        rows = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        rows = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        rows = paginator.page(paginator.num_pages)

    context["rows"] = rows

    return render_to_response('users/list.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='/access-denied/')
def form(request, pk=None):
    if request.POST:
        if pk:
            target = User.objects.get(pk=pk)
            form = UserForm(request.POST, instance=target)
        else:
            form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            form.save_m2m()
            return HttpResponseRedirect('/user/list')
    else:
        if pk:
            target = User.objects.get(pk=pk)
            form = UserForm(instance=target)
        else:
            form = UserForm()

    context.update(csrf(request))
    context['form'] = form

    return render_to_response('users/form.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='/access-denied/')
def details(request, pk):
    context["row"] = User.objects.get(pk=pk)

    return render_to_response('users/details.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='/access-denied/')
def delete(request, pk):
    entry = User.objects.get(pk=pk)
    entry.delete()

    return HttpResponseRedirect('/users/list')