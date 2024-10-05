from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from cats.models import Cat, Breed


class CatSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Cat"""

    breed = serializers.ReadOnlyField(source="breed.name")
    age_in_month = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Cat
        fields = (
            "id",
            "color",
            "breed",
            "description",
            "age_in_month",
            "rating",
        )

    def get_age_in_month(self, obj) -> int:
        """Возраст в месяцах"""
        return obj.get_age_in_month()

    def get_rating(self, obj) -> int:
        if not obj.rating:
            return 0
        return obj.rating


class CatWriteSerializer(CatSerializer):
    """Сериализатор для создания и редактирования записи о кошке"""

    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())

    class Meta:
        model = Cat
        fields = CatSerializer.Meta.fields + ("birth_date",)

    def to_representation(self, instance):
        return CatSerializer(instance).data


class CatRatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )


class BreedSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Breed"""

    class Meta:
        model = Breed
        fields = ("id", "name")
