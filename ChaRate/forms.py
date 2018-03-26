from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ChaRate.models import UserProfile, Movie, TV, Comment, Character

class UserForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=True, help_text='Insert Name.')
    email = forms.EmailField(max_length=254, required= True, help_text='Required. Inform a valid email address.')
    #password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','name', 'email', 'password1','password2')

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

class AddTvForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter the Title here and select the Genre from the dropdown",
    widget=forms.TextInput(attrs={'placeholder': 'Enter title here....'}))

    class Meta:
        model = TV
        fields = ('name', 'genre')

class AddMovForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter the Title here and select the Genre from the dropdown",
    widget=forms.TextInput(attrs={'placeholder': 'Enter title here....'}))

    class Meta:
        model = Movie
        fields = ('name', 'genre')

class add_comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('writer', 'character', 'content')

class createCharForm(forms.ModelForm):
    name = forms.CharField(required=True,max_length=20, help_text="Please enter the Character Name")
    picture = forms.ImageField(required=True, help_text="Choose an image to upload")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Character
        fields = ('name', 'picture')
