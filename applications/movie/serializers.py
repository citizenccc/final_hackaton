from rest_framework import serializers

from applications.movie.models import Movie, MovieImage
from applications.review.serializers import ReviewSerializer


class MovieImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieImage
        fields = ['image', ]
    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)

        else:
            url = ''
        return url

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = self._get_image_url(instance)
        return rep


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) != 0:
            rep['total_rating'] = sum(total_rating)/len(total_rating)
        else:
            rep['total_rating'] = ''
        rep['images'] = MovieImageSerializer(MovieImage.objects.filter(movie=instance.id), many=True,
                                               context=self.context).data
        rep['reviews'] = ReviewSerializer(instance.review.filter(movie=instance.id), many=True).data
        return rep