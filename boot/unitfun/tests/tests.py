from django.test import TestCase
from faker import Faker
from unitfun.models import Category, Product
from .categ_factory import CategoryFactory


class BasicUser(TestCase):

    def setUp(self) -> None:
        self.faker = Faker()

        self.categ = Category()
        self.categ.name = 'speeloed voor katten'
        self.categ.save()

        self.category = CategoryFactory(parent=self.categ)
        self.category.save()
        self.category2 = CategoryFactory(parent=self.categ)
        self.category2.save()
        self.category3 = CategoryFactory()
        self.category3.save()

        self.product = Product(
            title=self.faker.sentence(nb_words=2),
            description=self.faker.sentence(nb_words=12),
            categ=self.categ,
            price=2.44

        )
        self.product.save()

    def test_fields(self):
        """ check whether categ slug correct"""
        self.assertEqual(self.categ.parent, None)
        self.assertEqual(self.category.parent, self.categ)


