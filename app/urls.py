from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter


router = DefaultRouter()

router.register(r'cars', CarListViewSet, basename='cars')
router.register(r'movies', MovieViewSet, basename='movies')


urlpatterns = [
    path('', include(router.urls)),
    # path('movies/', MovieListView.as_view(), name='movies'),
    # path('movies/<int:pk>/', MovieDetailView.as_view(), name='movies_detail'),
    # path('create/', MovieCreateView.as_view(), name='movies_create'),


]
