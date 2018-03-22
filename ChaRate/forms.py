from django import forms
from django.contrib.auth.models import User
from ChaRate.models import UserProfile, Movie, TV, Comment, Character

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ()

#class linkMovieForm(forms.ModelForm):
    #movies = Movie.objects.all()

    #movie = forms.ChoiceField(choices=[(x, slugify(x)) for x in movies], required=False)
    #class Meta:
       # model =  Movie
       # fields = ('movie')

#class linkTvForm(forms.ModelForm):
#    shows = TV.objects.all()
#    show = forms.ChoiceField(choices=[(x, slugify(x)) for x in shows], required=False)
#    class Meta:
#        model = TV
#        fields = ('show')

#class AddTvForm(forms.ModelForm):
#    name = forms.CharField(widget=forms, help_text="Please enter the Title of the TV Show")

#    class Meta:
#        model = TV
#        fields = ('name', 'genre')

#class AddMovForm(forms.ModelForm):
#    name = forms.CharField(widget=forms, help_text="Please enter the Title of the Movie")

#    class Meta:
#        model = Movie
#        fields = ('name', 'genre')
#
class add_comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('writer', 'character', 'content')

class createCharForm(forms.ModelForm):
    name = forms.CharField(required=True,max_length=20, help_text="Please enter the Character Name")
    picture = forms.ImageField(required=True, help_text="Choose an image to upload")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Character
        fields = ('name', 'picture', 'likes')
