from rest_framework import generics
from movies.models import Movies
from movies.serializers import MoviesSerializer


class MoviesListCreate(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class MoviesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
