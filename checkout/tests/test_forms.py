from django.test import TestCase

from ..forms import OrderForm


class OrderFormTests(TestCase):
    def test_order_form(self):
        orderForm = OrderForm({
            'full_name': 'test',
            'email': 'test@gmail.com',
            'phone_number': '0123456789',
            'street_address1': '123 fake street',
            'town_or_city': 'somewhere',
            'country': 'IE'})
        self.assertIn('test@gmail.com', orderForm.as_p())

    def test_empty_form(self):
        orderForm = OrderForm({'form': ''})
        self.assertFalse(orderForm.is_valid())
        self.assertEqual(orderForm.errors['full_name'], [u'This field is required.'])
