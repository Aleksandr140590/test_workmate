import datetime

from django.contrib.auth import get_user_model
from faker import Faker
from factory.django import DjangoModelFactory
from factory import LazyAttribute
import factory

from cats.constants import COLOR_CHOICES
from cats.models import Cat, Breed

User = get_user_model()
fake = Faker("ru-RU")


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = LazyAttribute(lambda x: fake.user_name())
    first_name = LazyAttribute(lambda a: f"Test_{fake.first_name()}")
    email = LazyAttribute(lambda a: fake.unique.safe_email())
    last_name = LazyAttribute(lambda a: fake.last_name())
    is_active = True
    password = "User007!"


class CatFactory(DjangoModelFactory):
    class Meta:
        model = Cat

    color = LazyAttribute(
        lambda a: fake.random_choices([i[0] for i in COLOR_CHOICES], 1)[0]
    )
    birth_date = LazyAttribute(
        lambda a: datetime.datetime.strptime(fake.date(), "%Y-%m-%d").date()
    )
    description = LazyAttribute(lambda a: fake.text())
    breed = LazyAttribute(
        lambda a: fake.random_choices(Breed.objects.all(), 1)[0]
    )

    @factory.post_generation
    def author(self, create, extracted, **kwargs):
        if extracted:
            self.author = extracted
        if create:
            self.save(update_fields=["author"])
