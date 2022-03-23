
from rest_framework import generics, filters
from django_filters import rest_framework
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from applications.movie.models import Movie
from applications.movie.serializers import MovieSerializer

class MovieRatingFilter(rest_framework.FilterSet):
    min_rating = rest_framework.NumberFilter(field_name='rating', lookup_expr='gte')
    max_rating = rest_framework.NumberFilter(field_name='rating', lookup_expr='lte')

    class Meta:
        model = Movie
        fields = [
            'min_rating',
            'max_rating',
            'category',
        ]

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = MovieRatingFilter
    search_fields = ['title', 'description', ]

    def get_serializer_context(self):
        return {'request': self.request}

class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
