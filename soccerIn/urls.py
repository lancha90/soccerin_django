from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'soccerIn.views.home', name='home'),
    # url(r'^soccerIn/', include('soccerIn.foo.urls')),
    
    url(r'^$','api.views.get_all_user', name='user'),
    url(r'^get_info_user$','api.views.get_info_user', name='get_info_user'),
    url(r'^update_info_user$','api.views.update_info_user', name='update_info_user'),
    url(r'^add_user$','api.views.add_user', name='add_user'),

    url(r'^add_event$','api.views.add_event', name='add_event'),
    url(r'^get_my_event$','api.views.get_my_event', name='get_my_event'),
    url(r'^get_all_event$','api.views.get_all_event', name='get_all_event'),

    url(r'^add_team$','api.views.add_team', name='add_team'),
    url(r'^get_my_team$','api.views.get_my_team', name='get_my_team'),
    url(r'^get_all_team$','api.views.get_all_team', name='get_all_team'),
    url(r'^add_user_team$','api.views.add_user_team', name='add_user_team'),
    
    url(r'^get_user_friends$','api.views.get_user_friends', name='get_user_friends'),
    url(r'^add_user_friend$','api.views.add_user_friend', name='add_user_friend'),
    
    url(r'^get_user_message$','api.views.get_user_message', name='get_user_message'),
    url(r'^add_user_message$','api.views.add_user_message', name='add_user_message'),
    
    url(r'^get_all_field$','api.views.get_all_field', name='get_all_field'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
