from rest_framework import serializers

from cats.models import Cat, Breed


class CatSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Cat"""

    breed = serializers.ReadOnlyField(source="breed.name")
    age_in_month = serializers.SerializerMethodField()

    class Meta:
        model = Cat
        fields = ("id", "color", "breed", "description", "age_in_month")

    def get_age_in_month(self, obj):
        """Возраст в месяцах"""
        return obj.get_age_in_month()


class CatWriteSerializer(CatSerializer):
    """Сериализатор для создания и редактирования записи о кошке"""

    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())

    class Meta:
        model = Cat
        fields = CatSerializer.Meta.fields + ("birth_date",)

    def to_representation(self, instance):
        return CatSerializer(instance).data


class BreedSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Breed"""

    class Meta:
        model = Breed
        fields = ("id", "name")
