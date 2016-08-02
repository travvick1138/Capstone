from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

import datetime

# Create your models here.
class Image(models.Model):
    # A file that is that is .png or .jpeg for use to create a .cbz
    imagefile = models.FileField(upload_to='images/%Y/%m/%d')
    name = models.CharField(max_length=255, validators=[MaxLengthValidator(255)], blank=False)
    # --Front cover
    # -- pg1, pg2, pg3, etc
    # --Back Cover
    owner_id = models.ForeignKey(User)
    # foreign key = Creator
    def __str__(self):
        return self.name
