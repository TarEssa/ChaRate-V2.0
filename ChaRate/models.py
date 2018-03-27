from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    genre = models.CharField(max_length=20,choices=Genre_Choices)
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
    genre = models.CharField(max_length=20,choices=Genre_Choices)
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(TV, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'TV Shows'

    def __str__(self):
        return self.name


# class Character(models.Model):
#     name = models.CharField(max_length=128, unique = True)
#     likes = models.IntegerField(default=0)
#     likedBy = models.ManyToManyField(Profile)
#     picture = models.ImageField(upload_to='character_images', blank=True)
#     movies = models.ManyToManyField(Movie)
#     tvshows = models.ManyToManyField(TV)
#     slug = models.SlugField(blank=True, unique=True)

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Character, self).save(*args, **kwargs)

#     def __str__(self): 
#         return self.name               

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    CommentCount = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Character(models.Model):
    name = models.CharField(max_length=128, unique = True)
    #ID = models.IntegerField(unique = True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    likedBy = models.ManyToManyField(Profile)
    picture = models.ImageField(upload_to='character_images', blank=True)
    movies = models.ManyToManyField(Movie)
    tvshows = models.ManyToManyField(TV)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Character, self).save(*args, **kwargs)

    def __str__(self): 
        return self.name

class Comment(models.Model):
    writer = models.CharField(max_length=150)
    character = models.ForeignKey(Character)
    content = models.CharField(max_length=250)
    written_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name