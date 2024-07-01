from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from movies.models import Movies
from movies.serializers import MoviesSerializer
from app.permissions import GlobalDefaultPermission


class MoviesListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class MoviesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
