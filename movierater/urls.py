from django.urls import path
from .views import *

urlpatterns = [
    path('', get_movies, name="home"),
    path('create', add_movie, name="create-movie"),
    path('update/<str:pk>/', update_movie, name="update-movie"),
    path('delete/<str:pk>/', delete_movie, name="delete-movie"),

]
