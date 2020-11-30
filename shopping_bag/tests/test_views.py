from django.test import TestCase


class ShoppingBagViewTests(TestCase):

    # Main Page
    def test_main_page(self):
        response = self.client.get("/shopping_bag/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shopping_bag/shopping_bag.html")
