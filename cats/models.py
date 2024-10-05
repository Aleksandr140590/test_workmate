from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models
from datetime import date

from cats.constants import COLOR_CHOICES

User = get_user_model()


class Breed(models.Model):
    """Модель породы кошек"""

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Порода кошки"
        verbose_name_plural = "Породы кошек"

    def __str__(self):
        return self.name


class Cat(models.Model):
    """Модель кошки"""

    color = models.CharField(
        verbose_name="Цвет", max_length=20, choices=COLOR_CHOICES
    )
    breed = models.ForeignKey(
        Breed, verbose_name="Порода", on_delete=models.CASCADE
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения",
        validators=[
            MaxValueValidator(date.today),
        ],
    )
    description = models.TextField(verbose_name="Описание", max_length=500)
    author = models.ForeignKey(
        User, verbose_name="Автор", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Кошка"
        verbose_name_plural = "Кошки"

    def get_age_in_month(self):
        today = date.today()
        age_in_months = (
            12 * (today.year - self.birth_date.year)
            + (today.month - self.birth_date.month)
            - (1 if today.day < self.birth_date.day else 0)
        )
        return age_in_months

    def __str__(self):
        return f"{self.breed}, {self.get_age_in_month()}, {self.color}"


class CatRating(models.Model):
    """Модель рейтинга кошки"""

    user = models.ForeignKey(
        User, verbose_name="Владелец", on_delete=models.CASCADE
    )
    cat = models.ForeignKey(
        Cat, verbose_name="Кошка", on_delete=models.CASCADE
    )
    value = models.IntegerField(
        verbose_name="Рейтинг",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
        unique_together = (("user", "cat"),)

    def __str__(self):
        return f"{self.user} - {self.cat} - {self.value}"
