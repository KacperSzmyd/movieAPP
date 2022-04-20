from django.contrib import admin
from .models import Actor, Rate, Movie

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Rate)
