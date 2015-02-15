#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import logout
from core.forms.account_login import UserLoginForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def login(request):
    error = None
    if request.POST:
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/default/index/')
            else:
                error = True
        else:
            error = True
    else:
        form = UserLoginForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form
    args['error'] = error

    return render_to_response('account/login.html', args, context_instance=RequestContext(request))

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/account/login/')