from faker.providers import BaseProvider
from faker import Faker
from .categ_list import CATEGORIES

class Provider(BaseProvider):
    def ecomm_categs(self):
        return self.random_element(CATEGORIES)


