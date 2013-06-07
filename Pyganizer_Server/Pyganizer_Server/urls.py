from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'Pyganizer_Server.views.home', name='home'),

                       url(r'^login/$', 'user_management.views.login_user', name='login'),
                       url(r'^registration/$', 'user_management.views.registration_user', name='registration'),
                       url(r'^logout/$', 'user_management.views.logout_user', name='logout'),

                       url(r'^stats/$', 'user_management.views.user_stats', name='stats'),
                       url(r'^users_all/$', 'user_management.views.users_all', name='users_all'),

                       url(r'^add_friend/$', 'user_management.views.add_friend', name='add_friend'),

                       url(r'^show_friends/$', 'user_management.views.show_friends', name='show_friends'),
                       url(r'^add_user_to_friend/$', 'user_management.views.add_user_to_friend',
                           name='add_user_to_friend'),
                       url(r'^add_message/$', 'message_management.views.add_message', name='add_message'),
                       url(r'^add_event/$', 'message_management.views.add_event', name='add_event'),
                       url(r'^send_msg_to_friend_form/$', 'message_management.views.send_msg_to_friend_form',
                           name='send_msg_to_friend_form'),
                       url(r'^send_msg_to_friend/$', 'message_management.views.send_msg_to_friend',
                           name='send_msg_to_friend'),
                       url(r'^show_my_messages/$', 'message_management.views.show_my_messages',
                           name='show_my_messages'),
                       url(r'^add_sticky_note/$', 'message_management.views.add_sticky_note', name='add_sticky_note'),
                       url(r'^add_sticky_note_form/$', 'message_management.views.add_sticky_note_form',
                           name='add_sticky_note_form'),

                       url(r'^insert_label/$', 'user_management.views.insert_label', name='insert_label'),
                       # url(r'^Pyganizer_Server/', include('Pyganizer_Server.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^say_hello/', 'pyganizer_calendar.views.sayhello'),

                       )
