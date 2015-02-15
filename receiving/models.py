#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from receiving_category.models import ReceivingCategory


class Receiving(models.Model):
    receiving_category = models.ForeignKey(ReceivingCategory, verbose_name="Kategorija primanja")
    amount = models.DecimalField(decimal_places=2, max_digits=11, verbose_name="Iznos primanja")
    date_of_receiving = models.DateField(verbose_name="Datum primanja")
    received_by = models.ForeignKey(User, related_name="receiving_received_by", verbose_name="Primaoc")
    description = models.TextField(verbose_name="Opis", blank=True)

    created_by = models.ForeignKey(User, related_name="receiving_created_by", verbose_name="Unio")
    creation_datetime = models.DateTimeField(verbose_name="Vrijeme unosa")

    deleted = models.NullBooleanField(verbose_name="Obrisano", blank=True, null=True)
    deleted_datetime = models.DateTimeField(verbose_name="Vrijeme brisanja", blank=True, null=True)
    deleted_by = models.ForeignKey(User, related_name="receiving_deleted_by", verbose_name="Obrisao", blank=True, null=True)

    def __unicode__(self):
        return self.receiving_category.name

    class Meta:
        ordering = ['-pk']
        db_table = "receiving"