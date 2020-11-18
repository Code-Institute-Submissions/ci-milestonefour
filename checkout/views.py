from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(request, "There's nothing in your shopping bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HgUHCLephuOaa0VDJ92CMddW6Rsthl0GJV76Qle2juMV0LVO5vKpUJ0H7mU5PubmpFkI6brFcK698zsUGalNyAo00jorTqarp',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
