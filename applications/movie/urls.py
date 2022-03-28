from django.urls import path

from applications.movie.views import MovieListView, MovieDetailView, FavoriteView

urlpatterns = [
    path('', MovieListView.as_view()),
    path('<int:pk>/', MovieDetailView.as_view()),
    path('<int:pk>/favorite/', FavoriteView.as_view())
]