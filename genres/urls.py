from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.GenresListCreateView.as_view(),
         name='genres-list-create'),
    path('genres/<int:pk>/', views.GenresRetrieveUpdateDestroyView.as_view(),
         name='genres-retrieve-update-destroy'),
]
