#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from cost_category.models import CostCategory
from cost_subcategory.models import CostSubcategory


class CostName(models.Model):
    cost_category = models.ForeignKey(CostCategory, verbose_name="Kategorija troška")
    cost_subcategory = models.ForeignKey(CostSubcategory, null=True, blank=True, verbose_name="Podkategorija troška")
    name = models.CharField(max_length=1024, verbose_name="Naziv")

    deleted = models.NullBooleanField(verbose_name="Obrisano", blank=True, null=True)
    deleted_datetime = models.DateTimeField(verbose_name="Vrijeme brisanja", blank=True, null=True)
    deleted_by = models.ForeignKey(User, related_name="cost_name_deleted_by", verbose_name="Obrisao", blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
        db_table = "cost_name"