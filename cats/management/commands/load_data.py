from random import randint

from django.core.management import BaseCommand
from django.contrib.auth import get_user_model

from cats.models import Breed, Cat, CatRating
from cats.utils import factory

User = get_user_model()


class Command(BaseCommand):
    help = "Loads test data"

    def handle(self, *args, **options):
        with open("cats/utils/breeds.txt", "r") as f:
            breeds = []
            for line in f.readlines():
                breeds.append(Breed(name=line.strip()))
            try:
                Breed.objects.bulk_create(breeds)
            except:
                pass
        if len(User.objects.all()) > 1:
            print("There is data in DB")
            return
        users = factory.UserFactory.create_batch(10)
        cats_build = []
        for user in users:
            cats_factory = factory.CatFactory.build_batch(5, author=user)
            cats_build += cats_factory
        Cat.objects.bulk_create(cats_build)
        cats = Cat.objects.all()
        rating = []
        for cat in cats:
            for i in range(5):
                rating.append(
                    CatRating(
                        cat=cat,
                        user=users[randint(0, len(users) - 1)],
                        value=randint(1, 5),
                    )
                )
        CatRating.objects.bulk_create(rating, ignore_conflicts=True)
        print("Test data loaded")
