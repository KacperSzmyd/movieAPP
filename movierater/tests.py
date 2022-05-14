from decimal import Decimal
import datetime

from movierater.models import Movie, Review
from django.contrib.auth.models import User
from django.test import TestCase


def create_dummy_movies():
    Movie.objects.create(title="Avatar 2", release_year=2022, description="")
    Movie.objects.create(title="Harry Potter", release_year=2002, description="hp desc...")
    Movie.objects.create(title="Harry Potter 2", release_year=2004, description="hp desc...", imdb_rating=10.23)
    Movie.objects.create(title="Harry Potter 3", release_year=2004, description="hp desc...", imdb_rating=10.23,
                         premiere_date="2020-11-10")


class MovieTestCase(TestCase):
    def setUp(self):
        create_dummy_movies()

    def test_creating_movie(self):
        avatar_2 = Movie.objects.get(title="Avatar 2")
        harry_potter = Movie.objects.get(title="Harry Potter")
        harry_potter_2 = Movie.objects.get(title="Harry Potter 2")
        harry_potter_3 = Movie.objects.get(title="Harry Potter 3")

        self.assertEqual(avatar_2.title, "Avatar 2")
        self.assertEqual(avatar_2.release_year, 2022)
        self.assertEqual(avatar_2.description, "")
        self.assertEqual(harry_potter.release_year, 2002)
        self.assertEqual(harry_potter.description, "hp desc...")
        self.assertEqual(harry_potter_2.release_year, 2004)
        self.assertEqual(harry_potter_2.description, "hp desc...")
        self.assertEqual(harry_potter_2.imdb_rating, Decimal('10.23'))
        self.assertEqual(harry_potter_3.premiere_date, datetime.date(2020, 11, 10))


class ReviewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        movie = Movie.objects.create(title="dummy", release_year=2137, description="")
        Review.objects.create(author=user, body="Review body", stars=4, movie=movie)

    def test_creating_review(self):
        movie = Movie.objects.get(title="dummy")
        reviews = movie.review_set.all()
        review = movie.review_set.get(body="Review body")

        self.assertEqual(reviews.count(), 1)
        self.assertEqual(review.author.username, "testuser")
        self.assertEqual(review.body, "Review body")
        self.assertEqual(review.stars, 4)
        self.assertEqual(review.movie, movie)


class ActorTestCase(TestCase):
    def setUp(self):
        create_dummy_movies()

    def test_adding_actors_to_movie(self):
        avatar_2 = Movie.objects.get(title="Avatar 2")

        avatar_2.actors.create(name="John", surname="Brown")
        avatar_2.actors.create(name="Johny", surname="Cash")
        avatar_2.actors.create(name='Bony', surname='Ann')

        self.assertEqual(str(avatar_2.actors.get(name='John')), 'John Brown')
        self.assertEqual(str(avatar_2.actors.get(name='Johny')), 'Johny Cash')
        self.assertEqual(avatar_2.actors.all().count(), 3)
