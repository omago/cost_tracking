#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class ToDo(models.Model):
    task = models.TextField(max_length=11, verbose_name="Zadatak")
    date_to = models.DateField(verbose_name="Rok za izvršenje", null=True, blank=True)
    assignee = models.ForeignKey(User, related_name="todo_assignee", verbose_name="Izvršitelj")

    finished = models.NullBooleanField(verbose_name="Završeno")
    finished_datetime = models.DateTimeField(verbose_name="Datum završetka", null=True, blank=True)

    created_by = models.ForeignKey(User, related_name="todo_created_by", verbose_name="Unio", null=True, blank=True)
    creation_datetime = models.DateTimeField(verbose_name="Vrijeme unosa", null=True, blank=True)

    deleted = models.NullBooleanField(verbose_name="Obrisano", blank=True, null=True)
    deleted_datetime = models.DateTimeField(verbose_name="Vrijeme brisanja", blank=True, null=True)
    deleted_by = models.ForeignKey(User, related_name="todo_deleted_by", verbose_name="Obrisao", blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
        db_table = "todo"