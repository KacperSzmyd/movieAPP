from .serializers import ActorSerializer, MovieSerializer
from movierater.models import Movie, Actor
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_routes(request):
    routes = [
        'GET /api',
        'GET /api/movies',
        'GET /api/movies/:id',
        'GET /api/actors'
    ]
    return Response(routes)


@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.all()
    movie_serializer = MovieSerializer(movies, many=True)
    return Response(movie_serializer.data)


@api_view(['GET'])
def get_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    movie_serializer = MovieSerializer(movie, many=False)
    return Response(movie_serializer.data)


@api_view(['GET'])
def get_actors(request):
    actors = Actor.objects.all()
    actor_serializer = ActorSerializer(actors, many=True)
    return Response(actor_serializer.data)


@api_view(['GET'])
def get_actor(request, pk):
    actor = Actor.objects.get(id=pk)
    actor_serializer = ActorSerializer(actor, many=False)
    return Response(actor_serializer.data)