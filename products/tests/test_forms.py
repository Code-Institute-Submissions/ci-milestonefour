from django.test import TestCase


from ..forms import ProductForm


class ProductFormTests(TestCase):
    def test_product_form(self):
        productForm = ProductForm()
        self.assertIn('label for="id_category"', productForm.as_p())
