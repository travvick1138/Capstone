from django import forms


class ImageForm(forms.Form):
    comicbook = forms.ModelMultipleChoiceField(queryset=Comicbook.objects.all())
    name = models.CharField(label='Name your page', max_length=255, validators=[MaxLengthValidator(255)], blank=False,)
    imagefile = forms.FileField(label='Select a file',)


class ComicbookNameForm(forms.Form):
    title = forms.CharField(max_length=60, label='Name your comicbook',)
