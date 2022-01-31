from random import randint

from django.core.management.base import BaseCommand

from faker import Faker
import factory
from factory.fuzzy import FuzzyChoice
from faker import Faker

from unitfun.tests.categ_factory import Provider
from unitfun.models import Category, Product


class Command(BaseCommand):
    """
        create fake data (faker/factory boy)
    """

    def handle(self, *args, **options):
        fk = Faker()
        fk.add_provider(Provider)

        for _ in range(17):
            # len(categs_list) == 15 |=> limit for unique values
            name = fk.unique.ecomm_categs()
            Category.objects.get_or_create(name=name)
        # create random id for category (let op in in range)

        for _ in range(10):
            categ_id = randint(50, 66)
            Product.objects.create(
                categ_id=categ_id,
                price=fk.pydecimal(left_digits=4, right_digits=2, min_value=0.00, max_value=1000),
                sale= False,
                # TODO FuzzyChoices
                # sale=FuzzyChoice(choices=[False, False, False, True]),
                title=fk.text(max_nb_chars=18),
                description=fk.text(max_nb_chars=50)

            )
        check_amount_categs = Category.objects.count()
        check_amount_prods = Product.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Current number categs in db is:{check_amount_categs}'))
        self.stdout.write(self.style.SUCCESS(f'Current number prods in db is:{check_amount_prods}'))
