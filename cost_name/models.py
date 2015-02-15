#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from cost_category.models import CostCategory
from cost_subcategory.models import CostSubcategory


class CostName(models.Model):
    cost_category = models.ForeignKey(CostCategory, verbose_name="Kategorija troška")
    cost_subcategory = models.ForeignKey(CostSubcategory, null=True, blank=True, verbose_name="Podkategorija troška")
    name = models.CharField(max_length=1024, verbose_name="Naziv")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
        db_table = "cost_name"