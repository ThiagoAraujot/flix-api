from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MoviesListCreateView.as_view(),
         name='movies-list-create'),
    path('movies/<int:pk>/', views.MoviesRetrieveUpdateDestroyView.as_view(),
         name='movies-retrieve-update-destroy'),
    path('movies/stats/', views.MovieStatsView.as_view(), name='movie-stats-view'),
]
