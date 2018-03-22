from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Movie(models.Model):
    Genre_Choices = (
        ('sci', 'Sci-Fi'),
        ('action', 'Action'),
        ('horror', 'Horror'),
        ('comedy', 'Comedy'),
        ('romance', 'Romance'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=128, unique = True)
    genre = models.CharField(max_length=20,choices=Genre_Choices, default='other')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class TV(models.Model):
    Genre_Choices = (
        ('sci', 'Sci-Fi'),
        ('action', 'Action'),
        ('horror', 'Horror'),
        ('comedy', 'Comedy'),
        ('romance', 'Romance'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=128, unique = True)
    genre = models.CharField(max_length=20,choices=Genre_Choices, default='other')
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(TV, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'TV Shows'

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=128, unique = True)
    #ID = models.IntegerField(unique = True)
    likes = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='character_images', blank=True)
    movies = models.ManyToManyField(Movie)
    tvshows = models.ManyToManyField(TV)

    def __str__(self): 
        return self.name

                

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    CommentCount = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username

class Comment(models.Model):
    writer = models.ForeignKey(UserProfile)
    character = models.ForeignKey(Character)
    content = models.CharField(max_length=250)

    def __str__(self):
        return self.name