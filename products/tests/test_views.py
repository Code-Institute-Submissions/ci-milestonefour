from django.test import TestCase


class ProductViewTests(TestCase):

    # Products Page
    def test_main_products_page(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    # Subscriptions Page
    def test_main_subscriptions_page(self):
        response = self.client.get("/products/subscriptions/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/subscriptions.html")

    # Add New Product without login
    def test_create_new_product(self):
        response = self.client.post("/products/add/", {"pk": 101, "model": "products.product", "fields": {"sku": "9876", "name": "ADD PRODUCT", "description": "TEST", "has_sizes": "True", "price": 10.99, "category": 1, "subscription": "False", "rating": 5, "image_url": "", "image": ""}}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")
