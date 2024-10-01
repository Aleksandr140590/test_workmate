from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models
from django.utils.datetime_safe import date

from cats.constants import COLOR_CHOICES

User = get_user_model()


class Breed(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Порода кошки"
        verbose_name_plural = "Породы кошек"

    def __str__(self):
        return self.name


class Cat(models.Model):
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    birth_date = models.DateField()
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Кошка"
        verbose_name_plural = "Кошки"

    def get_age(self):
        return (date.today() - self.birth_date).month

    def __str__(self):
        return f"{self.breed}, {self.get_age()}, {self.color}"


class CatRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
        unique_together = (("user", "cat"),)

    def __str__(self):
        return f"{self.user} - {self.cat} - {self.value}"
