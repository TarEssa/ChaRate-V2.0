from django.conf.urls import url
from django.contrib.auth import views as auth_views
from ChaRate import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),



    # View TV Shows & Movies:
    url(r'^movies/$', views.view_movies, name = 'view_movies'),
    url(r'^tvshows/$', views.view_tvshows, name = 'view_tvshows'),

    # Display a Movie or TV Show:
    url(r'^tvshows/(?P<tv_name_slug>[\w\-]+)/$', views.show_tvShow, name='tvpage'),
    url(r'^movies/(?P<mov_name_slug>[\w\-]+)/$', views.show_movie, name='movpage'),

    # Add a Movie or TV Show:
    url(r'^add_tv/$', views.add_tv, name='add_tv'),
    url(r'^add_mov/$', views.add_mov, name = 'add_mov'),

    # View a Character:
    url(r'^character/(?P<char_name_slug>[\w\-]+)/$', views.character, name='character'),

    url(r'character_browser/$', views.character_browser, name='character_browser'),

    # Add a Character:
    url(r'^add_character/$', views.add_character, name = 'add_character'),

    # Link a Character to a Movie:
    #url(r'^character/(?P<char_name_slug>[\w\-]+)/link_to_movie/$', 
    #views.linkMovie, name = 'link_tvshow'),

    # Link a Character to a TV Show:
    #url(r'^character/(?P<char_name_slug>[\w\-]+)/link_to_movie/$', 
    #views.linkTv, name = 'link_movie'),

    # Add a Comment:
    url(r'^character/(?P<char_name_slug>[\w\-]+)/add_comment/$', views.add_comment, name="add_comment"),

#   url(r'^tvshows/(?P<tv_name_slug>[\w\-]+)/add_character/$',
#      views.create_character, name='create_character'),
#    url(r'^movies/(?P<mov_name_slug>[\w\-]+)/add_character/$',
#        views.create_character, name='create_character'),




#    url(r'^movie/(?P<mov_name_slug>[\w\-]+)/(?P<character_name_slug>[\w\-]+)/$',
#        views.character, name='character'),


    # User Authentication:
    url(r'^accounts/login/$', auth_views.login, name='login'),
#    url(r'^login/$', views.user_login, name ='login'),
#    url(r'^register/$', views.register, name='register'),
#    url(r'^logout/$', views.user_logout, name='logout'),


    #restricted +/ logout
    # No restricted page required

    # Test for javascript comments --------------------
    url(r'^samplecharacter/$', views.sample_char, name='samplechar'),
    # -------------------------------------------------
]
