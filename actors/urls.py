from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.ActorsListCreateView.as_view(),
         name='actors-list-create'),
    path('actors/<int:pk>/', views.ActorsRetrieveUpdateDestroyView.as_view(),
         name='actors-retrieve-update-destroy'),
]
