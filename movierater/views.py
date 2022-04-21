from django.shortcuts import render, redirect
from .models import Movie, Actor, Rate
from .forms import MovieForm


def get_movies(request):
    movies = Movie.objects.all()
    context = {'movies': movies}

    return render(request, 'all-movies.html', context)


def add_movie(request):
    page = 'create'
    movie_form = MovieForm(request.POST or None)
    if movie_form.is_valid():
        movie_form.save()
        return redirect('home')

    context = {'movie_form': movie_form,
               'page': page}

    return render(request, 'movie_form.html', context)


def update_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    movie_form = MovieForm(request.POST or None, instance=movie)
    if movie_form.is_valid():
        movie_form.save()
        return redirect('home')

    context = {'movie': movie,
               'movie_form': movie_form}

    return render(request, 'movie_form.html', context)


def delete_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('home')

    context ={'movie': movie}

    return render(request, 'delete.html', context)