from rest_framework.serializers import ModelSerializer
from movierater.models import Actor, Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'premiere_date', 'imdb_rating', 'description']


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
