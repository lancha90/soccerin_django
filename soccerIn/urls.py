from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'soccerIn.views.home', name='home'),
    # url(r'^soccerIn/', include('soccerIn.foo.urls')),
    url(r'^$','api.views.get_all_user', name='user'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
