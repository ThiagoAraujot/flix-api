from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reviews.models import Reviews
from reviews.serializers import ReviewSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
