# -*- coding: utf-8 -*-
from django import forms

class ComicbookForm(forms.Form):
    comicfile = forms.FileField(
        label='Select a file',
        help_text='max. 1000 megabytes'
    )


        def __init__(self, arg):
            super(imageForm, self).__init__()
            self.arg = arg


class ImageForm(forms.Form):
    """docstring for imageForm"""
    imagefile = forms.FileField(
        label='Select a file',
        help_text='max. 1000 megabytes'

        def __init__(self, arg):
            super(imageForm, self).__init__()
            self.arg = arg
