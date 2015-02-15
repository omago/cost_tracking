#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=128, verbose_name="Naziv")
    contact_person = models.CharField(max_length=128, verbose_name="Kontakt osoba", null=True, blank=True)
    phone_number = models.CharField(max_length=128, verbose_name="Kontakt broj telefona", null=True, blank=True)
    email = models.EmailField(max_length=128, verbose_name="Kontakt e-mail", null=True, blank=True)
    address = models.CharField(max_length=128, verbose_name="Kontakt adresa", null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
        db_table = "seller"