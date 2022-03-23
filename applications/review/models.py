from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from applications.account.models import User
from applications.movie.models import Movie


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='review')
    product = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review')
    review = models.TextField()
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return self.product.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    review =models.ForeignKey(Review, on_delete=models.CASCADE, related_name='like')
    # movie = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='like', null=True)
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.like

