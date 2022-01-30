import factory
from unitfun.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'categ_name_{}'.format(n))
    # print('name', name)
