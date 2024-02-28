
from django.urls import include, path
from . import views


urlpatterns = [
    path('api/films', views.film_list),
    path('api/films/<int:pk>', views.film_detail),
]
