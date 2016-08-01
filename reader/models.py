from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

import datetime

# Create your models here.
class Comicbook(models.Model):
    #when creating a file I will need to set users as Publisher
    #A file that is already a .cbr, .cbz, or .cbt file
    #Meta Data
    comicfile = models.FileField(upload_to='documents/%Y/%m/%d')
    title = models.CharField(max_length=255, validators=[MaxLengthValidator(255)], blank=False)
    publisher = models.CharField(max_length=255, validators=[MaxLengthValidator(255)], blank=True)
    volume = models.CharField(max_length=255, validators=[MaxLengthValidator(255)], blank=True)
    publish_date = models.DateTimeField(auto_now=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    #private_content = This needs to refelect that this is purchased content and cannot be shared or if it is creator owb should be sharable
    owner_id = models.ForeignKey(User)
    #foreign key = Creator
    #set rating
        def __str__(self):
            return self.title

class image(models.Model):
    # A file that is that is .png or .jpeg for use to create a .cbz
    imagefile = models.FileField(upload_to='documents/%Y/%m/%d')
    name = models.CharField(max_length=255, validators=[MaxLengthValidator(255)], blank=False)
    # --Front cover
    # -- pg1, pg2, pg3, etc
    # --Back Cover
    owner_id = models.ForeignKey(User)
    # foreign key = user
    # foreign key = Creator
        def __str__(self):
            return self.name


class Creator(models.Model):
    #An extended user class with permissions to create and share comicbooks they have created
    ATTRIBUTES = (
        (0, "Enthusiast"),
        (1, "Writer"),
        (2, "Artist"),
        (3, "Inker"),
        (4, "Colorist"),
        (5, "Letterer"),
        )

    user = models.OneToOneField(User)
    attribute = MultipleChoiceField(default=0, choices=ATTRIBUTES)#Are you a Writer/Artist/Inker/letter/colorist?
    self_publisher_name = models.CharField(max_length=255, validators=[MaxLengthValidator(255)], user.first_name, user.last_name, "+Comic", attribute)#ex. travisRVick+comicArtist


class Reader(models.Model):
    user = models.OneToOneField(User)
