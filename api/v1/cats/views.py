from django_filters.rest_framework.backends import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view
from rest_framework import permissions
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from api.v1.cats.filters import CatFilter
from api.v1.cats.permissions import IsAuthor
from api.v1.cats.serializers import (
    CatSerializer,
    CatWriteSerializer,
    BreedSerializer,
)
from api.v1.schema_extensions import (
    CATS_API_SCHEMA_EXTENSIONS,
    BREEDS_API_SCHEMA_EXTENSIONS,
)
from cats.models import Cat, Breed


@extend_schema_view(**CATS_API_SCHEMA_EXTENSIONS)
class CatViewSet(ModelViewSet):
    """Вьюсет для модели Cat"""

    queryset = Cat.objects.select_related("breed").all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CatFilter

    def get_permissions(self):
        """Пермишены для вьюсета"""
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (
            permissions.IsAuthenticated(),
            IsAuthor(),
        )

    def get_serializer_class(self):
        """Сериализаторы для вьюсета"""
        if self.request.method in permissions.SAFE_METHODS:
            return CatSerializer
        return CatWriteSerializer

    def perform_create(self, serializer):
        """Создание записи Cat"""
        serializer.save(author=self.request.user)


@extend_schema_view(**BREEDS_API_SCHEMA_EXTENSIONS)
class BreedViewSet(ListModelMixin, GenericViewSet):
    """Вьюсет для модели Breed"""

    queryset = Breed.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = BreedSerializer
