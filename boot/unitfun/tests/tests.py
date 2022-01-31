from django.test import TestCase
from faker import Faker
from unitfun.models import Category, Product
from .categ_factory import CategoryFactory, ProductFactory
from .categ_list import CATEGORIES


class BasicUser(TestCase):

    def setUp(self) -> None:
        self.faker = Faker()
        # name = self.faker.ecomm_categs()
        # print('name is :',name)
        self.categ = Category()
        self.categ.name = 'speeloed voor katten'
        self.categ.save()

        self.category = CategoryFactory(parent=self.categ)
        print(self.category.name)
        self.category.save()
        self.category2 = CategoryFactory(parent=self.categ)
        print(self.category2.name)
        self.category2.save()
        self.category3 = CategoryFactory()
        print(self.category3.name)
        self.category3.save()

        self.product2 = ProductFactory()
        # print(self.product2.title)
        # print(self.product2.description)
        self.product3 = ProductFactory()
        self.product4 = ProductFactory()
        self.product5 = ProductFactory()
        # print(self.product5.title)
        # print(self.product5.description)

    def test_fields(self):
        """ check whether categ slug correct"""
        self.assertEqual(self.categ.parent, None)
        self.assertEqual(self.category.parent, self.categ)
