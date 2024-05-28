from django.shortcuts import render
from rest_framework import viewsets, status

from .serializers import *
from .models import *


class CarListViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer




# class MovieListView(ListAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieListSerializer




# class MovieDetailView(RetrieveAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieDetailSerializer
#     lookup_field = 'pk'
#
#
# class MovieCreateView(CreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieDetailSerializer




