from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# The Model For the movie
class Movie(models.Model):
    # Types for filtering Genres
    Genre_Choices = (
        ('sci', 'Sci-Fi'),
        ('action', 'Action'),
        ('horror', 'Horror'),
        ('comedy', 'Comedy'),
        ('romance', 'Romance'),
        ('other', 'Other'),
    )
    # Name of Movie
    name = models.CharField(max_length=128, unique=True)
    # Its genre
    genre = models.CharField(max_length=20, choices=Genre_Choices)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# The Model For the TV Shows
class TV(models.Model):
    # Types for filtering Genres
    Genre_Choices = (
        ('sci', 'Sci-Fi'),
        ('action', 'Action'),
        ('horror', 'Horror'),
        ('comedy', 'Comedy'),
        ('romance', 'Romance'),
        ('other', 'Other'),
    )
    # Name of Movie
    name = models.CharField(max_length=128, unique=True)
    # Its genre
    genre = models.CharField(max_length=20, choices=Genre_Choices)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(TV, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'TV Shows'

    def __str__(self):
        return self.name


# User Profile Model
class Profile(models.Model):
    # Added items to display on the Profile page
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CommentCount = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
# Function to update the profile when ever its accessed
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


# Character Model
class Character(models.Model):
    # Name
    name = models.CharField(max_length=128, unique=True)
    # No. of Likes
    likes = models.IntegerField(default=0)
    # No. Of Comments on the char
    comments = models.IntegerField(default=0)
    # liked by the users
    likedBy = models.ManyToManyField(Profile)
    # Picture of the Character
    picture = models.ImageField(upload_to='character_images', blank=True)
    # Link to the Movies if any
    movies = models.ManyToManyField(Movie)
    # link to Tv Shows if any
    tvshows = models.ManyToManyField(TV)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Character, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# Comment Model
class Comment(models.Model):
    # Name of the user that wrote ethe comment
    writer = models.CharField(max_length=150)
    # Link to character (Commented on)
    character = models.ForeignKey(Character)
    # Content of teh comment
    content = models.CharField(max_length=250)
    # Date and time of teh comment
    written_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
