from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models.signals import post_save

import datetime

# Create your models here.
def comicbook_image_path(instance, filename):
    return '{user}/{title}/{file}'.format(user=instance.comicbook.user, title=slugify(instance.comicbook.title), file=instance.imagefile)


# def save_group(sender, instance, created, **kwargs):
#     print(instance)
#     UserExtended.objects.create(user=instance)


class Comicbook(models.Model):
    title = models.CharField(max_length=60, validators=[MaxLengthValidator(60)], blank=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title


class Image(models.Model):
    # A file that is that is .png or .jpeg for use to create a .cbz
    name = models.CharField(max_length=255, validators=[MaxLengthValidator(255)], blank=False)
    imagefile = models.FileField(upload_to=comicbook_image_path)
    comicbook = models.ForeignKey(Comicbook)

    def __str__(self):
        return self.name


# class UserExtended(models.Model):
#     user = models.OneToOneField(User)
#     is_creator = models.BooleanField(default=0)
#
# post_save.connect(save_group, sender=User)
# class Creator(models.Model):
#     #An extended user class with permissions to create and share comicbooks they have created
#     ATTRIBUTES = (
#         (0, "Enthusiast"),
#         (1, "Writer"),
#         (2, "Artist"),
#         (3, "Inker"),
#         (4, "Colorist"),
#         (5, "Letterer"),
#         )
#
#     user = models.OneToOneField(User)
#     attribute = MultipleChoiceField(default=0, choices=ATTRIBUTES)#Are you a Writer/Artist/Inker/letter/colorist?
#     # self_publisher_name = models.CharField(max_length=255, validators=[MaxLengthValidator(255)], user, "+Comic", attribute)#ex. travisRVick+comicArtist
#
#
# class Reader(models.Model):
#     user = models.OneToOneField(User)
