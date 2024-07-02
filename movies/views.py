from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from movies.models import Movies
from reviews.models import Reviews
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


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movies.objects.all()
    
    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Reviews.objects.all().count()
        average_stars = Reviews.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
        
        return response.Response(
            data={
                'total_movies': total_movies,
                'movies_by_genre': movies_by_genre,
                'total_reviews': total_reviews,
                'average_stars': round(average_stars, 1) if average_stars else 0,
            },
            status=status.HTTP_200_OK
        )