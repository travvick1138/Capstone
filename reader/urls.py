from django.conf.urls import include, url
from reader import views

urlpatterns = [
    url(r'^$', views.instructions),
    # url(r'^list/$', views.list, name='reader-list'),
    url(r'^new/$', views.newcomic, name='reader-new'),
    url(r'^upload/$', views.upload, name='reader-upload'),
    url(r'^cbr/$', views.cbrview, name='reader-cbr'),
    url(r'^inst/$', views.instructions, name='reader-inst'),
    url(r'^(?P<comic>[\d]+)', views.presentation, name='reader-presentation'),
]
