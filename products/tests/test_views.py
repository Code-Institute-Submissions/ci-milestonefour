from django.test import TestCase


class ProductViewTests(TestCase):
    #
    # Product Tests
    #

    # Products Page
    def test_products_page(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    # Add Product
    def test_product_creation(self):
        response = self.client.post('/products/add/', {"pk": 101, "model": "products.product", "fields": {"sku": "9876", "name": "ADD PRODUCT", "description": "TEST", "has_sizes": "True", "price": 10.99, "category": 1, "subscription": "False", "rating":5, "image_url": "", "image": ""}})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")

    # Product Details
    def test_product_retrieval(self):
        response = self.client.get('/products/101/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")

    # Edit Product
    def test_product_change(self):
        response = self.client.get('/products/edit/101/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/edit_product.html")
        response = self.client.post('/products/edit/101/', {"pk": 101, "model": "products.product", "fields": {"sku": "9876", "name": "CHANGE PRODUCT", "description": "TEST", "has_sizes": "True", "price": 10.99, "category": 1, "subscription": "False", "rating": 5, "image_url": "", "image": ""}})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")

    # Delete Product
    def test_product_deletion(self):
        response = self.client.get('/products/delete/101/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    #
    # Subscription Tests
    #

    # Subscriptions Page
    def test_subscriptions_page(self):
        response = self.client.get("/products/subscriptions/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/subscriptions.html")

    # Add Subscription
    def test_subscription_creation(self):
        response = self.client.post('/products/add/', {"pk": 102, "model": "products.product", "fields": {"sku": "6789", "name": "TEST SUBSCRIPTION", "description": "TEST", "has_sizes": "False", "price": 10.99, "category": 2, "subscription": "True", "rating": 5, "image_url": "", "image": ""}})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/subscription_detail.html")

    # Subscription Details
    def test_subscription_retrieval(self):
        response = self.client.get('/products/subscriptions/102/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/subscription_detail.html")

    # Delete Subscription
    def test_subscription_deletion(self):
        response = self.client.get('/products/delete/102/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/subscriptions.html")
