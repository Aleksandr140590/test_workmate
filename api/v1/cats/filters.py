from django_filters.rest_framework import FilterSet, Filter

from cats.models import Cat


class CatFilter(FilterSet):
    """Фильтр сериализатора кошек"""

    breed = Filter(field_name="breed__name", lookup_expr="icontains")

    class Meta:
        model = Cat
        fields = ["breed"]
