from . import views
from django.conf.urls import include, patterns, url

urlpatterns = [
    url(r'^userstatistics/', include(patterns(
        'userstatistics.views',
        url(r'^$', 'userstatistics', name='userstatistics'),
    ))),
]
