from django.db import models

# Create your models here.
class Comicbook(models.Model):
    #when creating a file I will need to set users as Publisher
    #A file that is already a .cbr, .cbz, or .cbt file
    #Meta Data
    #Title =
    #Publisher =
    #Volume =
    #Publish_date =
    #Upload_date =
    #private_content = This needs to refelect that this is purchased content and cannot be shared or if it is creator owb should be sharable
    #foreign key = user
    #foreign key = Reader
    #foreign key = Creator
    #set rating
    pass

class image(models.Model):
    #A file that is that is .png or .jpeg for use to create a .cbz
    #name = perhaps we give a specific layout or a drop down like a list
    # --Front cover
    # -- pg1, pg2, pg3, etc
    # --Back Cover
    #foreign key = user
    #foreign key = Creator
    pass

class library(models.Model):
    #Rating = list?
    #design a rating system for the comics people create see cbldf.org to see what is available.
    #A returned list of Comicbooks and/or images separated into 2 list by types perhaps we would do AJAX calls and build them on the frontend
    # potential connection with outside db like dropbox, google drive, or onedrive
    pass

class Creator(models.Model):
    #An extended user class with permissions to create and share comicbooks they have created
    #Type = Are you a Writer/Artist/Inker/letter/colorist?
    #Self Publisher name = (ex. travisRVick+comicArtist)
    pass

class Reader(models.Model):
    pass
