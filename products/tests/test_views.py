from django.test import TestCase


class ProductViewTests(TestCase):
    def test_index_page(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    # def test_product_creation(self):
    #     response = self.client.post('/add/', {})
    #     self.assertEqual(response.status_code, 200)

    # def test_product_retrieval(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)