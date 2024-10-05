from django.db.models import Avg
from django_filters.rest_framework.backends import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from api.v1.cats.filters import CatFilter
from api.v1.cats.permissions import IsAuthor
from api.v1.cats.serializers import (
    CatSerializer,
    CatWriteSerializer,
    BreedSerializer,
    CatRatingSerializer,
)
from api.v1.schema_extensions import (
    CATS_API_SCHEMA_EXTENSIONS,
    BREEDS_API_SCHEMA_EXTENSIONS,
)
from cats.models import Cat, Breed, CatRating


@extend_schema_view(**CATS_API_SCHEMA_EXTENSIONS)
class CatViewSet(ModelViewSet):
    """Вьюсет для модели Cat"""

    filter_backends = (DjangoFilterBackend,)
    filterset_class = CatFilter

    def get_queryset(self):
        queryset = Cat.objects.select_related("breed").annotate(
            rating=Avg("catrating__value")
        )
        return queryset

    def get_permissions(self):
        """Пермишены для вьюсета"""
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        if self.action == "rating":
            return (permissions.IsAuthenticated(),)
        return (
            permissions.IsAuthenticated(),
            IsAuthor(),
        )

    def get_serializer_class(self):
        """Сериализаторы для вьюсета"""
        if self.request.method in permissions.SAFE_METHODS:
            return CatSerializer
        if self.action == "rating":
            return CatRatingSerializer
        return CatWriteSerializer

    def perform_create(self, serializer):
        """Создание записи Cat"""
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["POST"])
    def rating(self, request, pk):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        rating = validated_data.get("rating")
        if CatRating.objects.filter(cat=pk, user=self.request.user).exists():
            raise ValidationError("Вы уже выставили рейтинг этой кошке.")
        cat = Cat.objects.get(id=pk)
        CatRating.objects.create(cat=cat, user=request.user, value=rating)
        return CatSerializer(cat).data


@extend_schema_view(**BREEDS_API_SCHEMA_EXTENSIONS)
class BreedViewSet(ListModelMixin, GenericViewSet):
    """Вьюсет для модели Breed"""

    queryset = Breed.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = BreedSerializer
