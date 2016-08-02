from django.conf.urls import include, url
from reader import views

urlpatterns = [
    url(r'^$', views.list),
    url(r'^list/$', views.list, name='reader-list'),
]
