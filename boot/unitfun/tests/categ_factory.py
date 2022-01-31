import factory
import faker.providers
from factory.fuzzy import FuzzyDecimal, FuzzyChoice, FuzzyText
from faker import Faker
from unitfun.models import Category, Product
from .categ_list import CATEGORIES
from .prod_list import PRODUCTS


class Provider(faker.providers.BaseProvider):
    """ create custom class with custom method based on self.random_element(...)"""

    def ecomm_categs(self):
        return self.random_element(CATEGORIES)

    def ecomm_prods(self):
        return self.random_element(PRODUCTS)


fk = Faker()
fk.add_provider(Provider)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    # name = factory.Sequence(lambda n: 'categ_name_{}'.format(n))
    name = fk.ecomm_categs()


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = ' '.join(fk.words(nb=2))
    description = FuzzyText(length=10)
    # description = ' '.join(fk.words(nb=5))
    categ = factory.SubFactory(CategoryFactory)
    price = fk.pydecimal(left_digits=4, right_digits=2, min_value=0.00, max_value=1000)
    sale = FuzzyChoice(choices=[False, False, False, True])

    # @factory.post_generation
    # def after(obj,create,extracted,**kwargs):
    #     if not create:
    #         return
    #     print('do smth tomorrow')
    #     obj.title + some rand
