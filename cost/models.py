#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from cost_category.models import CostCategory
from cost_subcategory.models import CostSubcategory
from cost_name.models import CostName
from seller.models import Seller


class Cost(models.Model):
    cost_category = models.ForeignKey(CostCategory, verbose_name="Kategorija troška")
    cost_subcategory = models.ForeignKey(CostSubcategory, blank=True, null=True, verbose_name="Podkategorija troška")
    cost_name = models.ForeignKey(CostName, blank=True, null=True, verbose_name="Naziv troška")
    amount = models.DecimalField(decimal_places=2, max_digits=11, verbose_name="Iznos troška")
    quantity = models.DecimalField(decimal_places=2, max_digits=11, verbose_name="Količina")
    paid_by = models.ForeignKey(User, related_name="cost_paid_by", verbose_name="Platio")
    date_of_cost = models.DateField(verbose_name="Datum troška")
    seller = models.ForeignKey(Seller, verbose_name="Prodavatelj", blank=True, null=True)
    attachment = models.FileField(verbose_name="Prilog", blank=True, upload_to="uploads")
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