from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from ChaRate.models import Character, Movie, TV
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



def index(request):
    characters = Character.objects.order_by('-likes')[:5]
    # most_discussed = Character.objects.order_by('-comments')[:1]
    context_dict = {'characters': characters}  # 'most_comments': most_discussed}
    return render(request, 'ChaRate/index.html', context=context_dict)


def about(request):
    return render(request, 'ChaRate/about.html', {'characters'})


@login_required
def link_movie(request, char_name_slug):
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

            return show_charecter(request, char_name_slug)
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
            return show_character(request, char_name_slug)
    return render(request, 'ChaRate/link_tv.html', context=context_dict)


@login_required
def Account(request, ):
    comments = Comment.objects.filter(writer=request.user)
    characters = UserProfile.objects.CommentCount.get(user=request.user)
    context_dict = {'comments': len(comments), 'characters': characters}
    return render(request, 'ChaRate/account.html', context=context_dict)


def filter_tv(request):
    TVshows = TV.objects.all()
    context_dict = {'TVShows': TVShows}
    return render(request, 'ChaRate/character.html', context_dict)


def filter_mov(request):
    movies = Movie.objects.all()
    context_dict = {'movies': movies}
    return render(request, 'ChaRate/character.html', context_dict)


def search(request):
    context_dict = {}
    character = Character.objects.all()
    context_dict['character'] = character
    return render(request, 'ChaRate/character.html', context_dict)


def show_character(request, Character_name_slug):
    context_dict = {}
    try:

        character = Character.objects.get(slug=Character_name_slug)
        movie = Character.objects.filter(character=character)
        TVshows = TV.objects.filter(character=character)
        context_dict['Name'] = character.name
        context_dict['Movies'] = movie
        context_dict['TVshows'] = TVshows
    except Character.DoesNotExist:
        context_dict['Movies'] = None
        context_dict['TVshows'] = None

    return render(request, 'ChaRate/character.html', context_dict)


def show_movie(request, movie_name_slug):
    context_dict = {}
    try:
        movie = Movie.objects.get(slug=movie_name_slug)
        characters = Character.objects.filter(movie=movie)
        context_dict['Movie'] = movie
        context_dict['Characters'] = characters

    except Movie.DoesNotExist:
        context_dict['movies'] = None
        context_dict['characters'] = None

    return render(request, 'ChaRate/movpage.html', context_dict)


def show_tvShow(request, tvshow_name_slug):
    context_dict = {}
    try:
        TvShow = TV.objects.get(slug=tvshow_name_slug)
        characters = characters.objects.filter(TvShow=TvShow)
        context_dict['tvshow'] = tvshow
        context_dict['Characters'] = characters

    except Category.DoesNotExist:
        context_dict['tvshow'] = None
        context_dict['characters'] = None

    return render(request, 'ChaRate/tvpage.html', context_dict)


@login_required
def add_tv(request):
    form = AddTvForm()
    model = TV

    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return filter_tv(request)
        else:

            print(form.errors)

    return render(request, 'ChaRate/add_tv.html', {'form': form})


@login_required
def add_mov(request):
    form = AddMovForm()
    model = Movie

    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return filter_mov(request)
        else:

            print(form.errors)

    return render(request, 'ChaRate/add_mov.html', {'form': form})


@login_required
def add_comment(request, Character_name_slug):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.writer = UserProfile.objects.get(user=request.user)

            form.save(commit=True)

            return show_character(request, Character_name_slug)
        else:

            print(form.errors)

    return render(request, 'ChaRate/add_comment.html', {'form': form})


# @login_required
# def add_characterTv(request, tvshow_name_slug):
#  try:
#   tvShow = TV.objects.get(slug=tvshow_name_slug)
#  except tvShow.DoesNotExist:
#      tvShow = None
#  form = TVForm()
#  if request.method == 'POST':
#   form = tvForm(request.POST)
#   if form.is_valid():
#    if tvShow:
#      character = form.save(commit=False)
#      character.likes = 0
#      character.save()
#      return show_category(request, tvshow_name_slug)
#  else:
#     print(form.errors)
#     context_dict = {'form':form, 'tvShow': tvShow}
#  return render(request, 'ChaRate/add_page.html', context_dict)


@login_required
def add_character(request, CHAR_name_slug):
    try:
        char = Character.objects.get(slug=CHAR_name_slug)
    except Character.DoesNotExist:
        char = None
    form = createCharForm()
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character.likes = 0
            character.save()
            return show_category(request, CHAR_name_slug)
    else:
        print(form.errors)
        context_dict = {'form': form, 'character': char}
    return render(request, 'ChaRate/create_character.html', context_dict)


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
        return render(request, 'ChaRate/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


    # ------------------------------------
