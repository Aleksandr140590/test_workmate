from django.contrib import admin

from cats.models import Cat, Breed


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    """Админка для модели Cat"""

    list_display = ("id", "breed", "color")
    fields = (
        "color",
        "breed",
        "birth_date",
        "description",
        "age",
        "rating",
        "author",
    )
    readonly_fields = ("rating", "age")

    @admin.display(description="Рейтинг")
    def rating(self, obj):
        """Пересчет рейтинга"""
        values = obj.catrating.values_list("value", flat=True)
        return float(sum(values) / len(values))

    @admin.display(description="Возраст")
    def age(self, obj):
        """Возраст в месяцах"""
        if obj.birth_date:
            age = obj.get_age_in_month()
            if age % 10 <= 0:
                return "0 месяцев"
            elif age % 10 == 1 and (age < 10 or age > 14):
                return f"{age} месяц"
            elif age % 10 <= 4 and (age < 10 or age > 14):
                return f"{age} месяца"
            return f"{age} месяцев"
        return "0 месяцев"


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    """Админка для модели Breed"""

    list_display = ("id", "name")
