from django.core.management.base import BaseCommand

from faker import Faker
from unitfun.tests.categ_factory import Provider
from unitfun.models import Category


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
        check_amount_categs = Category.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Current number categs in db is:{check_amount_categs}'))
