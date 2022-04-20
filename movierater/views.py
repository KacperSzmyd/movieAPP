from django.shortcuts import render
from .models import Movie, Actor, Rate

def get_movies(request):
    movies = Movie.objects.all()
    context = {'movies': movies}

    return render(request, 'all-movies.html', context)