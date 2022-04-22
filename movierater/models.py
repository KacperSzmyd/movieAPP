from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    release_year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default="")
    premiere_date = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2,
                                      null=True, blank=True)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)

    def title_with_release_year(self):
        return "{} ({})".format(self.title, self.release_year)

    def __str__(self):
        return self.title_with_release_year()


class Rate(models.Model):
    review = models.TextField(default="", blank=True)
    stars = models.PositiveSmallIntegerField(default=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Actor(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    movies = models.ManyToManyField(Movie, related_name="actors")