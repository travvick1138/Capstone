from django import forms
from .models import Image, Comicbook


class ImageForm(forms.Form):
    comicbook = forms.ModelMultipleChoiceField(label='Select your Comicbook', queryset=Comicbook.objects.all(),)
    name = forms.CharField(label='Name your page', max_length=255,)
    imagefile = forms.FileField(label='Select a file',)


class ComicbookNameForm(forms.Form):
    title = forms.CharField(max_length=60, label='Name your comicbook',)
