#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from cost_category.models import CostCategory

class CostSubcategory(models.Model):
    cost_category = models.ForeignKey(CostCategory, verbose_name="Kategorija troška")
    name = models.CharField(max_length=128, verbose_name="Naziv")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
        db_table = "cost_subcategory"