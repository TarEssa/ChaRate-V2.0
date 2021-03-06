import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charate_project.settings')

import django

django.setup()

from ChaRate.models import Character, Movie, TV, Comment


def populate():
    # create dictionary's for each movie , tv show and character
    movies = [
        {"name": "Spider-Man: Homecoming",
         "genre": "Action"},
        {"name": "Iron-Man 2",
         "genre": "Sci-Fi"},
        {"name": "Star-Trek",
         "genre": "Sci-Fi"},
        {"name": "Star Wars: A New Hope",
         "genre": "Sci-Fi"}
    ]

    shows = [
        {"name": "Agents of S.H.I.E.L.D",
         "genre": "Action"},
        {"name": "Game of Thrones",
         "genre": "Other"},
        {"name": "How I Met Your Mother",
         "genre": "Comedy"}
    ]

    chars = [
        {"name": "Tony Stark",
         "comments": 2,
         "likes": 25,
         "movies": ["Spider-Man: Homecoming", "Iron-Man 2"],
         "tvshows": []},
        {"name": "Peter Coulson",
         "comments": 1,
         "likes": 3,
         "movies": ["Iron-Man 2"],
         "tvshows": ["Agents of S.H.I.E.L.D"]},
        {"name": "Spock",
         "comments": 3,
         "likes": 12,
         "movies": ["Star-Trek"],
         "tvshows": []},
        {"name": "Tyrion Lannister",
         "comments": 6,
         "likes": 25,
         "movies": [],
         "tvshows": ["Game of Thrones"]},
        {"name": "Daenerys Targaryen",
         "comments": 6,
         "likes": 25,
         "movies": [],
         "tvshows": ["Game of Thrones"]},
        {"name": "Barney Stinson",
         "comments": 6,
         "likes": 25,
         "movies": [],
         "tvshows": ["How I Met Your Mother"]},
        {"name": "Darth Vader",
         "comments": 6,
         "likes": 25,
         "movies": ["Star Wars: A New Hope"],
         "tvshows": []},
    ]



    # add movies to db
    for film in movies:
        add_movie(film["name"], film["genre"])

    # add shows to db
    for tv in shows:
        add_tv(tv["name"], tv["genre"])



    # add characters to db
#    for char in chars:
#        c = Character.objects.get_or_create(name=char["name"], likes=0, comments=0)
#        if (char["movies"] != ""):
#            for film in char['movies']:
#                c.movies.add(Movie.objects.get(name=film))
#        else:
#            for show in char['tvshows']:
#                c.tvshows.add(Movie.objects.get(name=show))
#        c.save()


def add_movie(name, genre):
    f = Movie.objects.get_or_create(name=name, genre=genre)[0]
    f.genre = genre
    f.save()
    return f


def add_tv(name, genre):
    t = TV.objects.get_or_create(name=name, genre=genre)[0]
    t.genre = genre
    t.save()
    return t

def add_char(name , comments, likes, show):
    lis = ['tvshow', 'movie']
    cc = any(lis)
    c = Character.objects.get_or_create(name=name,cc=show) [0]


# Start execution here!
if __name__ == '__main__':
    print("Starting ChaRate population script...")
    populate()
