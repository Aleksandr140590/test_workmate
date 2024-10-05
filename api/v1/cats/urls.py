from django.urls import include, path
from rest_framework import routers

from api.v1.cats.views import CatViewSet, BreedViewSet

router = routers.DefaultRouter()
router.register("cats", CatViewSet, basename="cats")
router.register("breeds", BreedViewSet, basename="breeds")


urlpatterns = [
    path("", include(router.urls)),
]
