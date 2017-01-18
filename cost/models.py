#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from cost_category.models import CostCategory


class Cost(models.Model):
    cost_category = models.ForeignKey(CostCategory, verbose_name="Kategorija troška")
    amount = models.DecimalField(decimal_places=2, max_digits=11, verbose_name="Iznos troška")
    paid_by = models.ForeignKey(User, related_name="cost_paid_by", verbose_name="Platio")
    date_of_cost = models.DateField(verbose_name="Datum troška")
    description = models.TextField(verbose_name="Opis", blank=True)

    created_by = models.ForeignKey(User, related_name="cost_created_by", verbose_name="Unio")
    creation_datetime = models.DateTimeField(verbose_name="Vrijeme unosa")

    deleted = models.NullBooleanField(verbose_name="Obrisano", blank=True, null=True)
    deleted_datetime = models.DateTimeField(verbose_name="Vrijeme brisanja", blank=True, null=True)
    deleted_by = models.ForeignKey(User, related_name="cost_deleted_by", verbose_name="Obrisao", blank=True, null=True)

    def __unicode__(self):
        return self.cost_category.name

    class Meta:
        ordering = ['-pk']
        db_table = "cost"
