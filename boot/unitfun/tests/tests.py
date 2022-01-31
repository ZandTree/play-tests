from django.test import TestCase
from faker import Faker
from unitfun.models import Category, Product
from .categ_factory import CategoryFactory, ProductFactory
from .categ_list import CATEGORIES


class BasicUser(TestCase):

    def setUp(self) -> None:
        self.faker = Faker()

        # print(self.faker.pydecimal(left_digits=4,right_digits=2,min_value=0.00,max_value=1000))
        # print(self.faker.word(ext_word_list=CATEGORIES))
        # print(self.faker.words(nb=3,ext_word_list=CATEGORIES,unique=True))

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
