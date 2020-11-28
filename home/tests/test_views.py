from django.test import TestCase


class HomeViewsTests(TestCase):

    # Home Page
    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    # Returns Page
    def test_returns_page(self):
        response = self.client.get("/returns/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/returns.html")

    # Delivery Page
    def test_delivery_page(self):
        response = self.client.get("/delivery/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/delivery.html")

    # Contact Page
    def test_contact_page(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/contact.html")
