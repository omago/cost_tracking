#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
from calendar import monthrange

from django.utils import timezone
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth.models import User

from cost.models import Cost
from cost_category.models import CostCategory
from receiving.models import Receiving
from to_do.models import ToDo

@login_required
def index(request):
    context = {'page_title': "Početna"}

    current_time = timezone.now()
    current_day = current_time.day
    current_month = current_time.month
    current_year = current_time.year

    receive_sum = Receiving.objects\
        .filter(date_of_receiving__month=current_month)\
        .filter(date_of_receiving__year=current_year)\
        .aggregate(Sum("amount"))

    total_receivings = receive_sum["amount__sum"] if receive_sum["amount__sum"] else 0
    total_receivings_percentage = total_receivings/100

    spendings_by_days = []

    for x in range(1, monthrange(current_year, current_month)[1] + 1):
        day_sum = Cost.objects\
            .filter(date_of_cost__day=x)\
            .filter(date_of_cost__month=current_month)\
            .filter(date_of_cost__year=current_year)\
            .aggregate(Sum("amount"))

        if day_sum["amount__sum"]:
            sum = day_sum["amount__sum"]
        else:
            sum = 0

        if sum > 0:
            height = 1 + int(sum/12)
        else:
            height = 1

        spendings_by_days.append({
            "date_url": "/cost/report?month=" + str(current_month) + "&day=" + str(x),
            "height": height,
            "day": x,
            "date": date(day=x, month=current_month, year=current_year),
            "sum": sum
        })

    spendings_by_categories = []
    total_spendings = 0
    cost_categories = CostCategory.objects.all()

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

        sum_percentage = 0

        if cost_sum["amount__sum"]:
            sum_percentage = cost_sum["amount__sum"]/total_receivings_percentage if total_receivings_percentage > 0 else 0

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

        receive_sum_amount = receive_sum["amount__sum"] if receive_sum["amount__sum"] else 0
        cost_sum_amount = cost_sum["amount__sum"] if cost_sum["amount__sum"] else 0

        left_to_spent = receive_sum_amount - cost_sum_amount
        spending_sum_percentage = receive_sum_amount/100

        spendings_by_users.append({"user": user.first_name,
                                   "user_id": user.pk,
                                   "user_link": "<a href='/cost/report?paid_by=" + str(user.pk) + "&month=" + str(current_month) + "'>" + user.first_name + "</a>",
                                   "receiving_sum": receive_sum["amount__sum"] if receive_sum["amount__sum"] else 0,
                                   "receiving_sum_percetange": spending_sum_percentage,
                                   "spending_sum": cost_sum_amount,
                                   "spending_sum_percentage": cost_sum_amount/spending_sum_percentage if cost_sum_amount and spending_sum_percentage > 0 else 0,
                                   "left_to_spent": left_to_spent,
                                   "left_to_spent_percentage": left_to_spent/spending_sum_percentage if left_to_spent and spending_sum_percentage > 0 else 0})

    user_to_dos = ToDo.objects\
        .filter(finished__isnull=True)\
        .filter(assignee=request.user)\

    context["user_to_dos"] = user_to_dos
    context["spendings_by_days"] = spendings_by_days
    context["spendings_by_categories"] = spendings_by_categories
    context["spendings_by_users"] = spendings_by_users
    context["current_day"] = current_day
    context["current_month"] = current_month
    context["current_year"] = current_year
    context["total_receivings"] = total_receivings
    context["total_receivings_percentage"] = total_receivings_percentage
    context["avarage_spendings_per_day"] = total_spendings/current_day
    context["avarage_spendings_per_day_percentage"] = context["avarage_spendings_per_day"]/context["total_receivings_percentage"] if context["total_receivings_percentage"] > 0 else 0
    context["total_spendings"] = total_spendings
    context["total_spendings_percentage"] = total_spendings/context["total_receivings_percentage"] if context["total_receivings_percentage"] > 0 else 0
    context["left_to_spent"] = total_receivings - total_spendings
    context["left_to_spent_percentage"] = context["left_to_spent"]/context["total_receivings_percentage"] if context["total_receivings_percentage"] > 0 else 0

    return render_to_response('default/index.html', context, context_instance=RequestContext(request))


@login_required
def access_denied(request):
    context = {'page_title': "ACCESS DENIED"}
    return render_to_response('default/access_denied.html', context, context_instance=RequestContext(request))
