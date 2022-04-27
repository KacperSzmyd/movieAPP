from .forms import MovieForm, MyUserCreationForm, ReviewForm, ActorForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Movie, Actor, Review
from django.contrib import messages


def get_movies(request):
    movies = Movie.objects.all()
    context = {'movies': movies}

    return render(request, 'all-movies.html', context)


def get_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    reviews = movie.review_set.all()
    review_form = ReviewForm
    actors = movie.actors.all()
    if request.method == 'POST':
        stars = request.POST.get('stars')
        if stars > 5:
            stars = 5
        Review.objects.create(author=request.user,
                              body=request.POST.get('body'),
                              stars=stars,
                              movie=movie)
        return redirect('movie')

    context = {'movie': movie,
               'actors': actors,
               'reviews': reviews,
               'review_form': review_form}

    return render(request, 'movie.html', context)


@login_required(login_url='login')
def add_movie(request):
    movie_form = MovieForm(request.POST, request.FILES)

    if movie_form.is_valid():
        movie_form.save()
        return redirect('home')

    context = {'movie_form': movie_form}

    return render(request, 'movie_form.html', context)


@login_required(login_url='login')
def update_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    actors = movie.actors.all()
    movie_form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    actor_form = ActorForm(request.POST)

    if 'name' in request.POST or 'surname' in request.POST:
        actor, created = Actor.objects.get_or_create(name=request.POST.get('name'),
                                                     surname=request.POST.get('surname'))
        actor.movies.add(movie)
        actor.save()

    if movie_form.is_valid():
        movie_form.save()
        return redirect('home')

    context = {'movie': movie,
               'actors': actors,
               'movie_form': movie_form,
               'actor_form': actor_form}

    return render(request, 'movie_form.html', context)


@login_required(login_url='login')
def delete_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('home')

    context = {'movie': movie}

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
    user_creation_form = MyUserCreationForm(request.POST)
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


def get_actors(request):
    actors = Actor.objects.all()

    context = {'actors': actors}

    return render(request, 'actors.html', context)