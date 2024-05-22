from django.urls import path
from .views import *

urlpatterns = [
    path('cars/', CarListViewSet.as_view({'get': 'list'}), name='cars'),
    path('movies/', MovieListView.as_view(), name='movies'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movies_detail'),
    path('create/', MovieCreateView.as_view(), name='movies_create'),


]
