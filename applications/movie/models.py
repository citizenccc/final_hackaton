from django.db import models

from applications.category.models import Category


class Movie(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='movie')
    description = models.TextField()
    year = models.PositiveIntegerField()
    # rating = models.PositiveIntegerField()
    # old data
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # in_stock = models.BooleanField(default=True)
    # quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class MovieImage(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='movie_photo')

    def __str__(self):
        return self.movie.title
