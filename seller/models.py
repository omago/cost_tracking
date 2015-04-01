#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    name = models.CharField(max_length=128, verbose_name="Naziv")
    contact_person = models.CharField(max_length=128, verbose_name="Kontakt osoba", null=True, blank=True)
    phone_number = models.CharField(max_length=128, verbose_name="Kontakt broj telefona", null=True, blank=True)
    email = models.EmailField(max_length=128, verbose_name="Kontakt e-mail", null=True, blank=True)
    address = models.CharField(max_length=128, verbose_name="Kontakt adresa", null=True, blank=True)

    deleted = models.NullBooleanField(verbose_name="Obrisano", blank=True, null=True)
    deleted_datetime = models.DateTimeField(verbose_name="Vrijeme brisanja", blank=True, null=True)
    deleted_by = models.ForeignKey(User, related_name="seller_deleted_by", verbose_name="Obrisao", blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
        db_table = "seller"