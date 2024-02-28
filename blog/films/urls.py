from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('films', views.FilmView, basename='products')

urlpatterns = router.urls