import time

from django.db.models import Count, F
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from blog.films import models
from blog.films.serializers import FilmSerializer


class FilmView(ModelViewSet):
    model = models.Film
    serializer_class = FilmSerializer
    queryset = models.Film.objects.all()


