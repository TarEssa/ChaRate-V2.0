from django.contrib import admin
from ChaRate.models import Profile
from ChaRate.models import Character, TV, Movie, Comment


# Register your models here.
# Character Admin
class Char_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# Tv Admin
class TV_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# Movie Admin
class Movie_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# Admin Page View
admin.site.register(Profile)
admin.site.register(Character, Char_Admin)
admin.site.register(Movie, Movie_Admin)
admin.site.register(TV, TV_Admin)
