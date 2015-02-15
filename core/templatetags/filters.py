#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from django.template.defaultfilters import floatformat

register = template.Library()


def format(value, arg):
    """
    Alters default filter "stringformat" to not add the % at the front,
    so the variable can be placed anywhere in the string.
    """
    try:
        if value:
            return (unicode(arg)) % value
        else:
            return u''
    except (ValueError, TypeError):
        return u''

register.filter('format', format)


def dict_value(value, key):
    """
    Alters default filter "stringformat" to not add the % at the front,
    so the variable can be placed anywhere in the string.
    """
    try:
        if value:
            return value[key]
        else:
            return u''
    except (ValueError, TypeError):
        return u''

register.filter('dict_value', dict_value)


def list_value(value, key):
    """
    Alters default filter "stringformat" to not add the % at the front,
    so the variable can be placed anywhere in the string.
    """
    try:
        if value:
            return value[key]
        else:
            return u''
    except (ValueError, TypeError):
        return u''

register.filter('list_value', list_value)


def convert_to_string(value, empty_string=None):
    if value == "" and empty_string:
        value = empty_string
    try:
        return str(value)
    except UnicodeEncodeError:
        return value

register.filter('convert_to_string', convert_to_string)


@register.filter
def replace_comma_float_format(value, args):
    search = ","
    replace = "."

    value = floatformat(value, args)
    new_string = str(value).replace(search, replace)

    return new_string

register.filter('replace_comma_float_format', replace_comma_float_format)
