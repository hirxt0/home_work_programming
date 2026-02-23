from django.shortcuts import render, get_object_or_404
from .models import Movie, Personage, Starship


def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'tripshit/movies_list.html', {'movies': movies})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    characters = movie.characters.all()
    starships = movie.starships.all()
    context = {
        'movie': movie,
        'characters': characters,
        'starships': starships
    }
    return render(request, 'tripshit/movie_detail.html', context)


def characters_list(request):
    characters = Personage.objects.all()
    return render(request, 'tripshit/characters_list.html', {'characters': characters})


def character_detail(request, character_id):
    character = get_object_or_404(Personage, id=character_id)
    films = character.films.all()
    starships = character.starships.all()
    
    context = {
        'character': character,
        'films': films,
        'starships': starships
    }
    return render(request, 'tripshit/character_detail.html', context)


def starships_list(request):
    starships = Starship.objects.all()
    return render(request, 'tripshit/starships_list.html', {'starships': starships})

def starship_detail(request, ship_id):
    starship = get_object_or_404(Starship, id=ship_id)
    films = starship.films.all()
    pilots = starship.pilots.all()

    context = {
        'starship': starship,
        'films': films,
        'pilots': pilots
    }
    return render(request, 'tripshit/starship_detail.html', context)


def home(request):
    movies_count = Movie.objects.count()
    characters_count = Personage.objects.count()
    starships_count = Starship.objects.count()
    
    context = {
        'movies_count': movies_count,
        'characters_count': characters_count,
        'starships_count': starships_count,
    }
    return render(request, 'tripshit/home.html', context)