from django.test import TestCase
from faker import Faker
from unitfun.models import Category, Product

"""
class Product(models.Model):
    arrived_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', unique=True)
    unid = models.UUIDField(default=uuid.uuid4, editable=False)
    description = models.TextField()
    categ = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='prods')
    stock = models.BooleanField(default=True)
    new = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)

    price = models.DecimalField(max_digits=10, decimal_places=2)    

"""


class BasicUser(TestCase):

    def setUp(self) -> None:
        self.faker = Faker()
        self.categ = Category()
        self.categ.name = 'speeloed voor katten'
        self.categ.save()
        # seed vals
        #fake = Faker()
        #Faker.seed(4321)
        self.faker2 = Faker()
        self.faker2.seed_instance(98)
        self.categ2 = Category()
        self.categ2.name = self.faker2.sentence(nb_words=1)
        print('with seed categ:', self.categ2)
        self.categ2.save()

        self.product = Product(
            title=self.faker.sentence(nb_words=2),
            description=self.faker.sentence(nb_words=12),
            categ=self.categ,
            price=2.44

        )
        self.product.save()

    def tearDown(self) -> None:
        self.product.delete()
        self.categ.delete()

    def test_fields(self):
        """ check whether categ slug correct"""
        self.assertEqual(self.categ.slug, 'speeloed-voor-katten')
        self.assertEqual(self.categ.parent, None)
