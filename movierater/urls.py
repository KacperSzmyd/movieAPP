from django.urls import path
from .views import *

urlpatterns = [
    path('', get_movies, name="all-movies"),

]
