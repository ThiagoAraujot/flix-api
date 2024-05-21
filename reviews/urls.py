from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewListCreateView.as_view(),
         name='reviews-list-create'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(),
         name='reviews-retrieve-update-destroy'),
]
