import time

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.response import Response

from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view
from twisted.web._template_util import Redirect

from . import models, forms
from .serializers import FilmSerializer


class FilmDetailView(ListView):
    template_name = 'film_detail.html'
    model = models.Film

    def get_queryset(self):
        queryset = super(FilmDetailView, self).get_queryset()

        queryset = queryset.filter(id=self.kwargs.get('pk'))
        print(queryset.values())
        return queryset


@api_view(['DELETE'])
def Deletee(request, pk):
    film = models.Film.objects.get(id=pk)
    return render(request,'success.html' )


class FilmListView(ListView):
    model = models.Film
    template_name = 'films.html'
    queryset = models.Film.objects.all()

    def post(self, request, *args, **kwargs):
        form = forms.FilmsForm(request.POST)
        if form.is_valid():
            serializer = FilmSerializer(data=form.data)
            if serializer.is_valid():
                serializer.save()
            return HttpResponse('<h1>new Film</h1>')
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.FilmsForm()
        return context
