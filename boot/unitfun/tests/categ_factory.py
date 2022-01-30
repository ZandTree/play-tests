import factory
from factory.fuzzy import FuzzyDecimal, FuzzyChoice, FuzzyText
from faker import Faker
from unitfun.models import Category, Product

fk = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'categ_name_{}'.format(n))


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = FuzzyText(length=12)  # different for obj's
    description = factory.Faker('sentence')  # same for obj's
    categ = factory.SubFactory(CategoryFactory)
    price = FuzzyDecimal(.00, 1000.00, 2)
    sale = FuzzyChoice(choices=[False, False, False, True])

    # @factory.post_generation
    # def after(obj,create,extracted,**kwargs):
    #     if not create:
    #         return
    #     print('do smth tomorrow')
    #     obj.title + some random

