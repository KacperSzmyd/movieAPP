from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Movie, Review, Actor
from django.forms import ModelForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'release_year', 'description',
                  'premiere_date', 'imdb_rating', 'poster']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['stars', 'body']


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'surname', 'movies']
