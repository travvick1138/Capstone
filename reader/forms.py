# -*- coding: utf-8 -*-
from django import forms

class ComicbookForm(forms.Form):
    comicfile = forms.FileField(
        label='Select a file',
        help_text='max. 1000 megabytes'
    )
