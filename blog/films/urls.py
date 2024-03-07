
from django.urls import include, path
from . import views
from .views import FilmListView, FilmDetailView, Delete

urlpatterns = [
    path('api/films', FilmListView.as_view(), name='film'),
    path('api/film/<int:pk>', FilmDetailView.as_view()),
    path('api/film/delete/<int:pk>', views.Delete, name='delete'),

]
