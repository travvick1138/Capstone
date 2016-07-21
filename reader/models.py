from django.db import models

# Create your models here.
class Comicbook(models.Model):
    #when creating a file I will need to set users as Publisher
    #A file that is already a .cbr, .cbz, or .cbt file
    #Meta Data
    title = models.CharField(max_length=255, validators=[MaxLengthValidator(255)], blank=False)
    Publisher = models.CharField(max_length=255, validators=[MaxLengthValidator(255)], blank=True)
    Volume = models.CharField(max_length=255, validators=[MaxLengthValidator(255)], blank=True)
    Publish_date = models.DateTimeField(auto_now=True)
    Upload_date = models.DateTimeField(auto_now_add=True)
    #private_content = This needs to refelect that this is purchased content and cannot be shared or if it is creator owb should be sharable
    owner_id = models.ForeignKey(Reader)
    #foreign key = Reader
    #foreign key = Creator
    #set rating
        def __str__(self):
            return self.title

# class image(models.Model):
    #A file that is that is .png or .jpeg for use to create a .cbz
    #name = models.CharField(max_length=255, validators=[MaxLengthValidator(255)], blank=False)
    # --Front cover
    # -- pg1, pg2, pg3, etc
    # --Back Cover
    #foreign key = user
    #foreign key = Creator
        # def __str__(self):
        #     return self.name

# class library(models.Model):
#     #Rating = list?
#     #design a rating system for the comics people create see cbldf.org to see what is available.
#     #A returned list of Comicbooks and/or images separated into 2 list by types perhaps we would do AJAX calls and build them on the frontend
#     # potential connection with outside db like dropbox, google drive, or onedrive
#     pass

class Creator(models.Model):
    #An extended user class with permissions to create and share comicbooks they have created
    #Type = Are you a Writer/Artist/Inker/letter/colorist?
    #Self Publisher name = (ex. travisRVick+comicArtist)
    pass

class Reader(models.Model):
    pass
