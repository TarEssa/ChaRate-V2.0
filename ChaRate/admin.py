from django.contrib import admin
from ChaRate.models import Profile
from ChaRate.models import Character, TV, Movie, Comment

# Register your models here.
class Char_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class TV_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class Movie_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Profile)
admin.site.register(Character,Char_Admin)
admin.site.register(Movie,Movie_Admin)
admin.site.register(TV,TV_Admin)