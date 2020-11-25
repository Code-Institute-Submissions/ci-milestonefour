from django.test import TestCase

from ..models import Product


class ProductModelTests(TestCase):
    def test_done_default_to_false(self):
        product = Product(name="Test product", subscription=False)
        self.assertEqual(product.name, "Test product")
