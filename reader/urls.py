from django.conf.urls import patterns, include, url


urlpatterns = patterns('.views',
    url(r'^$', 'list', name='list'),
    url(r'^list/$', 'list', name='list'),
)
