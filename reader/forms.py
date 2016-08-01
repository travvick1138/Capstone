from django import forms

class ImageForm(forms.Form):
    imagefile = forms.FileField(
        label='Select a file',
    )
