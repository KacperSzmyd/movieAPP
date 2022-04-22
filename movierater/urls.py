from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', get_movies, name="home"),
    path('movie/<str:pk>/', get_movie, name="movie"),
    path('create', add_movie, name="create-movie"),
    path('update/<str:pk>/', update_movie, name="update-movie"),
    path('delete/<str:pk>/', delete_movie, name="delete-movie"),

    path('register/', register_page, name="register"),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name="logout"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
