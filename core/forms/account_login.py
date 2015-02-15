#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Korisničko ime'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Lozinka'}))