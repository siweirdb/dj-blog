
from django.urls import include, path
from . import views
from .views import FilmListView, FilmDetailView, Deletee

urlpatterns = [
    path('api/films', FilmListView.as_view(), name='film'),
    path('api/film/delete/<int:pk>', views.Deletee, name='deletee'),
    path('api/film/<int:pk>', FilmDetailView.as_view()),

]
