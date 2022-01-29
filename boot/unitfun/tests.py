from django.test import TestCase

from unitfun.models import Category

"""
Category
    name = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='name', unique=True)
    parent
    

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
        self.categ = Category()
        self.categ.name = 'speeloed voor katten'
        self.categ.save()

    def test_fields(self):
        """ check whether categ slug correct"""
        self.assertEqual(self.categ.slug, 'speeloed-voor-katten')
        self.assertEqual(self.categ.parent, None)
