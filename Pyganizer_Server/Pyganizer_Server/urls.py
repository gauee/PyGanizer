from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Pyganizer_Server.views.home', name='home'),
    url(r'^login/$', 'user_management.views.login_user', name='login'),
    url(r'^registration/$', 'user_management.views.registration_user', name='registration'),
    url(r'^logout/$', 'user_management.views.logout_user', name='logout'),
    url(r'^stats/$','user_management.views.user_stats',name='stats'),
    url(r'^users_all/$','user_management.views.users_all',name='users_all'),
    url(r'^add_message/$','message_management.views.add_message',name='add_message'),
    # url(r'^Pyganizer_Server/', include('Pyganizer_Server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
