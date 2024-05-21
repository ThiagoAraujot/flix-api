from django.contrib import admin
from django.urls import path
from genres.views import GenresListCreateView, GenresRetrieveUpdateDestroyView
from actors.views import ActorsListCreateView, ActorsRetrieveUpdateDestroyView
from movies.views import MoviesListCreate, MoviesRetrieveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),

    # Genres URLs
    path('genres/', GenresListCreateView.as_view(), name='genres-list-create'),
    path('genres/<int:pk>/', GenresRetrieveUpdateDestroyView.as_view(),
         name='genres-retrieve-update-destroy'),

    # Actors URLs
    path('actors/', ActorsListCreateView.as_view(), name='actors-list-create'),
    path('actors/<int:pk>/', ActorsRetrieveUpdateDestroyView.as_view(),
         name='actors-retrieve-update-destroy'),

    # Movies URLs
    path('movies/', MoviesListCreate.as_view(), name='movies-list-create'),
    path('movies/<int:pk>/', MoviesRetrieveUpdateDestroy.as_view(),
         name='movies-retrieve-update-destroy'),

]
