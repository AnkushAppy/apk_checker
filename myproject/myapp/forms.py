# -*- coding: utf-8 -*-

from django import forms


class DocumentForm(forms.Form):

    docfile = forms.FileField(
        label='Select a file'
    )

#class Apk_Form(forms.Form):

