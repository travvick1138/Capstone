# from django.db.models import get_models, get_app
from django.contrib import admin
# from django.contrib.admin.sites import AlreadyRegistered
from .models import Image, Comicbook

class ComicbookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Image)
admin.site.register(Comicbook, ComicbookAdmin)
# admin.site.register(UserExtended)
# def autoregister(*app_list):
#     for app_name in app_list:
#         app_models = get_app(app_name)
#         for model in get_models(app_models):
#             try:
#                 admin.site.register(model)
#             except AlreadyRegistered:
#                 pass
#
# autoregister('reader')
