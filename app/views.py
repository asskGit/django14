from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class CarListViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    # def list(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data)


class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer

    # def get(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True, context={'request': request})
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = 'pk'


class MovieCreateView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer




