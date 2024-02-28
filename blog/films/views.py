import time
from django.shortcuts import render
from rest_framework.response import Response
from . import models
from .serializers import FilmSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view
from django.db.models import Count, F
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, ViewSet

from . import models, serializers
from .serializers import FilmSerializer


# class FilmView(ViewSet):
#     def list(self, request):
#         queryset = models.Film.objects.all()
#         serializer = serializers.FilmSerializer(queryset, many=True)
#
#         return Response(serializer.data)
@api_view(['GET', 'PUT', 'DELETE'])
def film_detail(request, pk):
    try:
        film = models.Film.objects.get(pk=pk)
    except models.Film.DoesNotExist:
        return Response({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = FilmSerializer(film)
        return Response(tutorial_serializer.data)

    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = FilmSerializer(film, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        film.delete()
        return Response({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def film_list(request):
    films = models.Film.objects.all()

    if request.method == 'GET':
        film_serializer = serializers.FilmSerializer(films, many=True)
        return Response(film_serializer.data)

    if request.method == 'POST':
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
    return Response(status=400)
