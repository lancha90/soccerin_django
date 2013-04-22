from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'soccerIn.views.home', name='home'),
    # url(r'^soccerIn/', include('soccerIn.foo.urls')),
    
    url(r'^$','api.views.get_all_user', name='user'),
    url(r'^get_info_user$','api.views.get_info_user', name='get_info_user'),
    url(r'^add_user$','api.views.add_user', name='add_user'),

    url(r'^add_event$','api.views.add_event', name='add_event'),
    url(r'^get_my_event$','api.views.get_my_event', name='get_my_event'),
    
    url(r'^get_all_field$','api.views.get_all_field', name='get_all_field'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
