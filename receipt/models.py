#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from seller.models import Seller


class Receipt(models.Model):
    paid_by = models.ForeignKey(User, related_name="receipt_paid_by", verbose_name="Platio")
    date_of_receipt = models.DateField(verbose_name="Datum računa")
    seller = models.ForeignKey(Seller, verbose_name="Prodavatelj", blank=True, null=True)
    attachment = models.FileField(verbose_name="Prilog", blank=True, upload_to="uploads")
    description = models.TextField(verbose_name="Opis", blank=True)

    created_by = models.ForeignKey(User, related_name="receipt_created_by", verbose_name="Unio")
    creation_datetime = models.DateTimeField(verbose_name="Vrijeme unosa")

    deleted = models.NullBooleanField(verbose_name="Obrisano", blank=True, null=True)
    deleted_datetime = models.DateTimeField(verbose_name="Vrijeme brisanja", blank=True, null=True)
    deleted_by = models.ForeignKey(User, related_name="receipt_deleted_by", verbose_name="Obrisao", blank=True, null=True)

    def __unicode__(self):
        return "Račun " + str(self.pk)

    class Meta:
        ordering = ['-pk']
        db_table = "receipt"