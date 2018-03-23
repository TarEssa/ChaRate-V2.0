from django.conf.urls import url
from django.contrib.auth import views as auth_views
from ChaRate import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_tv/$', views.add_tv, name='add_tv'),
    url(r'^add_mov/$', views.add_mov, name = 'add_mov'),

    #2 of each kind for tv and movie but both link to same view
#    url(r'^tvpage/(?P<tv_name_slug>[\w\-]+)/$',
#        views.tvpage, name='tvpage'),
#    url(r'^movpage/(?P<mov_name_slug>[\w\-]+)/$',
#        views.movpage, name='movpage'),

#   url(r'^tvpage/(?P<tv_name_slug>[\w\-]+)/add_character/$',
#      views.create_character, name='create_character'),
#    url(r'^movpage/(?P<mov_name_slug>[\w\-]+)/add_character/$',
#        views.create_character, name='create_character'),


#    url(r'^tvpage/(?P<tv_name_slug>[\w\-]+)/(?P<character_name_slug>[\w\-]+)/$',
#        views.character, name='character'),
#    url(r'^movpage/(?P<mov_name_slug>[\w\-]+)/(?P<character_name_slug>[\w\-]+)/$',
#        views.character, name='character'),


    url(r'^accounts/login/$', auth_views.login, name='login'),
#    url(r'^login/$', views.user_login, name ='login'),
#    url(r'^register/$', views.register, name='register'),
#    url(r'^logout/$', views.user_logout, name='logout'),
    #restricted +/ logout
    # No restricted page required

    # Test for javascript comments --------------------
    url(r'samplecharacter/$', views.sample_char, name='samplechar'),
    # -------------------------------------------------
]
