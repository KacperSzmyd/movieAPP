from django.urls import path
from .views import *

urlpatterns = [
    path('', get_routes),
    path('movies/', get_movies),
    path('movies/<str:pk>/', get_movie),
    path('actors/', get_actors),
    path('actors/<str:pk>/', get_actor),
]