from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import Actor
from actors.serializers import ActorSerializer
from app.permissions import GlobalDefaultPermission


class ActorsListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
