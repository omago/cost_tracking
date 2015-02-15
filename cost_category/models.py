#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class CostCategory(models.Model):
    name = models.CharField(max_length=128, verbose_name="Naziv")
    monthly_budget = models.IntegerField(max_length=11, verbose_name="Mjesečni budget", null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
        db_table = "cost_category"