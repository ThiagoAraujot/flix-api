from genres.models import Genre
from rest_framework.permissions import IsAuthenticated
from genres.serializers import GenreSerializer
from rest_framework import generics
from app.permissions import GlobalDefaultPermission


class GenresListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenresRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
