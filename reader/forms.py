from django import forms

class ImageForm(forms.Form):
    imagefile = forms.FileField(
        label='Select a file',
    )


class ComicbookNameForm(forms.Form):
    title = forms.CharField(
        max_length=60,
        label='Name your comicbook',
    )
