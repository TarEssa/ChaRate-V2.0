from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from ChaRate.models import Character, Movie, TV
from ChaRate.forms import *
from ChaRate.forms import UserForm, UserProfileForm

# from django.db.utils import OperationalError
# format_list = [('', '(all)')]
# geom_type_list = [('', '(all)')]
# try:
#     format_list.extend([(i[0],i[0]) 
#         for i in Format.objects.values_list('name')])
#     geom_type_list.extend([(i[0],i[0]) 
#         for i in Geom_type.objects.values_list('name')])
# except OperationalError:
#     pass  # happens when db doesn't exist yet, views.py should be
#           # importable without this side effect

# ------Only a sample for  JavaScript comments------
def sample_char(request):
    return render(request, 'ChaRate/character_sample.html', {})
# --------------------------------------------------

def index(request):
    characters = Character.objects.order_by('-likes')[:5]
    # most_discussed = Character.objects.order_by('-comments')[:1]
    context_dict = {'characters': characters}  # 'most_comments': most_discussed}
    return render(request, 'ChaRate/index.html', context_dict)


def about(request):
    return render(request, 'ChaRate/about.html', {})


@login_required
def linkMovie(request, char_name_slug):
    try:
        character = Character.objects.get(slug=char_name_slug)
    except Character.DoesNotExist:
        character = None

    movies_list = Movie.objects.all()
    currentmovie = linkMovieForm()

    if request.method == 'POST':

        currentmovie = linkMovie(request.POST)

        if [character not in currentmovie.Character.all()]:
            currentmovie.Charecter.add(Charecter.objects.get(name=char_name_slug))

            return character(request, char_name_slug)
    return render(request, 'ChaRate/link_mov.html', context=context_dict)


@login_required
def linkTv(request, char_name_slug):
    try:
        character = Character.objects.get(slug=char_name_slug)
    except Character.DoesNotExist:
        character = None

    shows_list = TV.objects.all()
    currentshow = linkTvForm()

    if request.method == 'POST':

        currentshow = linkTvForm(request.POST)

        if [character not in currentmovie.Character.all()]:
            currentshow.Character.add(Character.objects.get(name=char_name_slug))
            return character(request, char_name_slug)
    return render(request, 'ChaRate/link_tv.html', context=context_dict)


@login_required
def Account(request, ):
    comments = Comment.objects.filter(writer=request.user)
    characters = UserProfile.objects.CommentCount.get(user=request.user)
    context_dict = {'comments': len(comments), 'characters': characters}
    return render(request, 'ChaRate/account.html', context=context_dict)


def view_tvshows(request):
    TVShows = TV.objects.all()
    context_dict = {'tvshows': TVShows}
    return render(request, 'ChaRate/tvfilter.html', context_dict)


def view_movies(request):
    movies = Movie.objects.all()
    context_dict = {'movies': movies}
    return render(request, 'ChaRate/movfilter.html', context_dict)


def search(request):
    context_dict = {}
    character = Character.objects.all()
    context_dict['character'] = character
    return render(request, 'ChaRate/character.html', context_dict)


def character(request, char_name_slug):
    context_dict = {}
    try:
        character = Character.objects.get(slug=char_name_slug)
        # movie = character.objects.get(movies)
        # TVshows = TV.objects.filter(character=character)
        context_dict['character'] = character
        context_dict['movies'] = character.movies
        context_dict['tvshows'] = character.tvshows
    except Character.DoesNotExist:
        context_dict['character'] = None
        context_dict['movies'] = None
        context_dict['tvshows'] = None

    return render(request, 'ChaRate/character.html', context_dict)

def character_browser(request):
    characters = Character.objects.all()
    context_dict = {'characters': characters}

    return render(request, 'ChaRate/character_browser.html', context_dict)

def show_movie(request, mov_name_slug):
    context_dict = {}
    try:
        movie = Movie.objects.get(slug=mov_name_slug)
        characters = Character.objects.filter(movies=movie)
        context_dict['movie'] = movie
        context_dict['characters'] = characters

    except Movie.DoesNotExist:
        context_dict['movies'] = None
        context_dict['characters'] = None

    return render(request, 'ChaRate/movpage.html', context_dict)


def show_tvShow(request, tv_name_slug):
    context_dict = {}
    try:
        tvshow = TV.objects.get(slug=tv_name_slug)
        characters = Character.objects.filter(tvshows=tvshow)
        context_dict['tvshow'] = tvshow
        context_dict['characters'] = characters

    except TV.DoesNotExist:
        context_dict['tvshow'] = None
        context_dict['characters'] = None

    return render(request, 'ChaRate/tvpage.html', context_dict)


@login_required
def add_tv(request):
    form = AddTvForm()
    model = TV

    if request.method == 'POST':
        form = AddTvForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return view_tvshows(request)
        else:

            print(form.errors)

    return render(request, 'ChaRate/add_tv.html', {'form': form})


@login_required
def add_mov(request):
     form = AddMovForm()
     model = Movie

     if request.method == 'POST':
         form = AddMovForm(request.POST)

         if form.is_valid():
             form.save(commit=True)

             return view_movies(request)
         else:

             print(form.errors)

     return render(request, 'ChaRate/add_mov.html', {'form': form})


@login_required
def add_comment(request, char_name_slug):
    try:
        character = Character.objects.get(slug=char_name_slug)
    except:
        character = None

    form = add_comment()
    if request.method == 'POST':
        form = add_comment(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.writer = request.user
            form.character = character
            form.save()

            return character(request, char_name_slug)
        else:

            print(form.errors)

    return render(request, 'ChaRate/add_comment.html', {'form': form, 'character': character})

@login_required
def add_character(request):
    # try:
        # char = Character.objects.get(slug=char_name_slug)
    # except Character.DoesNotExist:
    form = createCharForm()
    if request.method == 'POST':
        form = createCharForm(request.POST, request.FILES)
        if form.is_valid():
            # character.likes = 0
            character.picture = request.FILES['picture']
            form.save(commit=True)
            return character_browser(request)
    else:
        print(form.errors)
    return render(request, 'ChaRate/create_character.html', {'form': form})


def get_character_list(max_results=0, starts_with=''): 
    char_list = []
    if starts_with:
        char_list = Character.objects.filter(name__istartswith=starts_with)
    if max_results > 0:
        if len(char_list) > max_results:
            char_list = char_list[:max_results] 
    return char_list

def suggest_character(request): 
    char_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    char_list = get_character_list(8, starts_with)
    return render(request, 'ChaRate/chars.html', {'chars': char_list })

# User Authentication: ------------------------------------

def register(request):
    registered = False
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        # profile_form = UserProfileForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            registered = True
            login(request, user)


            # profile = profile_form.save(commit=False)
            # profile.user = user
            # if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']
        #            profile.save()
        #            registered = True
        #       else:
        #          print(user_form.errors, profile_form.errors)
    else:
        form = UserForm
        # profile_form = UserProfileForm()
    return render(request, 'ChaRate/registration_register',
                  {'form': form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your ChaRate account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


    # ------------------------------------
