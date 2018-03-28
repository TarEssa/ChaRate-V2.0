from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ChaRate.models import Profile, Movie, TV, Comment, Character

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required= True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ( 'bio', 'CommentCount', 'likes')

class linkMovieForm(forms.Form):
    movies = Movie.objects.all()
    try:
        movie = forms.ChoiceField(choices=[(x.slug, x) for x in movies], required=True)
    except:
        show = None
    class Meta:
        fields = ('movie',)

class linkTvForm(forms.Form):
    shows = TV.objects.all()
    try:
        show = forms.ChoiceField(choices=[(x.slug, x) for x in shows], required=True)
    except:
        show = None
    class Meta:
        shows = TV.objects.all()
        show = forms.ChoiceField(choices=[(x.slug, x) for x in shows], required=True)
        fields = ('show',)

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

class addComment(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    # writer = forms.CharField(widget=forms.HiddenInput())
    # character = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Comment
        fields = ('content',)

class createCharForm(forms.ModelForm):
    name = forms.CharField(required=True,max_length=20, help_text="Please enter the Character Name")
    picture = forms.ImageField(required=True, help_text="Choose an image to upload")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Character
        fields = ('name', 'picture')
