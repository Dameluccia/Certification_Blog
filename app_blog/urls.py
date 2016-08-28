from django.conf.urls import url,include


from .views import *


urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^draft/$', draft_list, name='draft_list'),
    url(r'^draft/(?P<slug>[\w-]+)/$', draft_detail, name='draft_detail'),
    url(r'^create/$', post_create, name='create'),
    url(r'^profile/(?P<id>\d+)/$', user_profile, name='profile'),
    url(r'^profile/(?P<id>\d+)/update$', user_update, name='user_update'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete$', post_delete, name='delete'),

]
