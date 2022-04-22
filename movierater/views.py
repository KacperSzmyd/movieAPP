from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .models import Movie, Actor, Rate
from django.contrib import messages
from .forms import MovieForm, MyUserCreationForm
from django.contrib.auth.decorators import login_required


def get_movies(request):
    movies = Movie.objects.all()
    context = {'movies': movies}

    return render(request, 'all-movies.html', context)


def get_movie(request, pk):
    movie = Movie.objects.get(id=pk)

    context = {'movie': movie,
               }

    return render(request, 'movie.html', context)


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


@login_required(login_url='login')
def delete_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('home')

    context ={'movie': movie}

    return render(request, 'delete.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Incorrect username OR password")

    context = {'page': page}

    return render(request, 'login-register.html', context)


def logout_page(request):
    logout(request)
    return redirect('home')


def register_page(request):
    user_creation_form = MyUserCreationForm(request.POST or None)
    if user_creation_form.is_valid():
        user = user_creation_form.save(commit=False)
        user.username = user.username.title()
        user.save()
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, "An error occurred during registration")

    context = {'form': user_creation_form}

    return render(request, 'login-register.html', context)