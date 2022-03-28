
from rest_framework import generics, filters, status
from django_filters import rest_framework
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.user.models import Profile
from applications.movie.models import Movie
from applications.movie.serializers import MovieSerializer

class MovieYearFilter(rest_framework.FilterSet):
    min_year = rest_framework.NumberFilter(field_name='year', lookup_expr='gte')
    max_year = rest_framework.NumberFilter(field_name='year', lookup_expr='lte')

    class Meta:
        model = Movie
        fields = [
            'min_year',
            'max_year',
            'category',
        ]

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = MovieYearFilter
    search_fields = ['title', 'description', ]

    def get_serializer_context(self):
        return {'request': self.request}

class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



class FavoriteView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, pk):
        print(Profile.objects.all())
        profile = Profile.objects.get(user=request.user.id)
        if profile.favorite.filter(id=pk).exists():
            profile.favorite.set(profile.favorite.exclude(id=pk))
            msg = 'Movie has been removed from favourites'
        else:
            profile.favorite.add(pk)
            profile.save()
            msg = "Movie has been added to favourites successfully"
        return Response(msg, status=status.HTTP_200_OK)