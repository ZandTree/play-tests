from django.test import TestCase
from faker import Faker
from unitfun.models import Category, Product
from .categ_factory import CategoryFactory, ProductFactory


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

        self.product2 = ProductFactory()
        self.product3 = ProductFactory()
        self.product4 = ProductFactory()
        self.product5 = ProductFactory()

    def test_fields(self):
        """ check whether categ slug correct"""
        self.assertEqual(self.categ.parent, None)
        self.assertEqual(self.category.parent, self.categ)
