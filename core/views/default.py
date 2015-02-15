#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.utils import timezone
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth.models import User

from cost.models import Cost
from cost_category.models import CostCategory
from receiving.models import Receiving

@login_required
def index(request):
    context = {'page_title': "Početna"}

    current_time = timezone.now()
    current_day = current_time.day
    current_month = current_time.month
    current_year = current_time.year

    cost_categories = CostCategory.objects.all()
    spendings_by_categories = []
    total_spendings = 0

    receive_sum = Receiving.objects\
        .filter(date_of_receiving__month=current_month)\
        .filter(date_of_receiving__year=current_year)\
        .aggregate(Sum("amount"))

    total_receivings = receive_sum["amount__sum"]
    total_receivings_percentage = total_receivings/100


    for cost_category in cost_categories:
        cost_sum = Cost.objects\
            .filter(date_of_cost__month=current_month)\
            .filter(date_of_cost__year=current_year)\
            .filter(cost_category=cost_category)\
            .aggregate(Sum("amount"))

        if cost_sum["amount__sum"]:
            total_spendings += cost_sum["amount__sum"]

        left_to_spent = 0
        if cost_category.monthly_budget and cost_sum["amount__sum"]:
            left_to_spent = cost_category.monthly_budget - cost_sum["amount__sum"]

        if cost_sum["amount__sum"]:
            sum_percentage = cost_sum["amount__sum"]/total_receivings_percentage

        spendings_by_categories.append({"category": cost_category.name,
                                        "category_id": cost_category.pk,
                                        "category_link": "<a href='/cost/report?cost_category_multiple=" + str(cost_category.pk) + "&month=" + str(current_month) + "'>" + cost_category.name + "</a>",
                                        "sum": cost_sum["amount__sum"],
                                        "sum_percentage": sum_percentage,
                                        "monthly_budget": cost_category.monthly_budget,
                                        "left_to_spent": left_to_spent})

    users = User.objects.all()
    spendings_by_users = []

    for user in users:
        cost_sum = Cost.objects\
            .filter(date_of_cost__month=current_month)\
            .filter(date_of_cost__year=current_year)\
            .filter(paid_by=user)\
            .aggregate(Sum("amount"))

        receive_sum = Receiving.objects\
            .filter(date_of_receiving__month=current_month)\
            .filter(date_of_receiving__year=current_year)\
            .filter(received_by=user)\
            .aggregate(Sum("amount"))

        left_to_spent = receive_sum["amount__sum"] - cost_sum["amount__sum"]
        spending_sum_percentage = receive_sum["amount__sum"]/100

        spendings_by_users.append({"user": user.first_name,
                                   "user_id": user.pk,
                                   "user_link": "<a href='/cost/report?paid_by=" + str(user.pk) + "&month=" + str(current_month) + "'>" + user.first_name + "</a>",
                                   "receiving_sum": receive_sum["amount__sum"],
                                   "receiving_sum_percetange": spending_sum_percentage,
                                   "spending_sum": cost_sum["amount__sum"],
                                   "spending_sum_percentage": cost_sum["amount__sum"]/spending_sum_percentage,
                                   "left_to_spent": left_to_spent,
                                   "left_to_spent_percentage": left_to_spent/spending_sum_percentage})

    context["spendings_by_categories"] = spendings_by_categories
    context["spendings_by_users"] = spendings_by_users
    context["current_day"] = current_day
    context["current_month"] = current_month
    context["current_year"] = current_year
    context["total_receivings"] = total_receivings
    context["total_receivings_percentage"] = total_receivings_percentage
    context["total_spendings"] = total_spendings
    context["total_spendings_percentage"] = total_spendings/context["total_receivings_percentage"]
    context["left_to_spent"] = total_receivings - total_spendings
    context["left_to_spent_percentage"] = context["left_to_spent"]/context["total_receivings_percentage"]

    return render_to_response('default/index.html', context, context_instance=RequestContext(request))


@login_required
def access_denied(request):
    context = {'page_title': "ACCESS DENIED"}
    return render_to_response('default/access_denied.html', context, context_instance=RequestContext(request))
