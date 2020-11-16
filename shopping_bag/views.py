from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_shopping_bag(request):
    """ A view that renders the shopping bag contents page """

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopping_bag = request.session.get('shopping_bag', {})

    if size:
        if item_id in list(shopping_bag.keys()):
            if size in shopping_bag[item_id]['items_by_size'].keys():
                shopping_bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {shopping_bag[item_id]["items_by_size"][size]}')
            else:
                shopping_bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your shopping bag')
        else:
            shopping_bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your shopping bag')
    else:
        if item_id in list(shopping_bag.keys()):
            shopping_bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {shopping_bag[item_id]}')
        else:
            shopping_bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your shopping bag')

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)


def update_shopping_bag(request, item_id):
    """Adjust the quantity of the product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopping_bag = request.session.get('shopping_bag', {})

    if size:
        if quantity > 0:
            shopping_bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {shopping_bag[item_id]["items_by_size"][size]}')
        else:
            del shopping_bag[item_id]['items_by_size'][size]
            if not shopping_bag[item_id]['items_by_size']:
                shopping_bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your shopping bag')
    else:
        if quantity > 0:
            shopping_bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {shopping_bag[item_id]}')
        else:
            shopping_bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your shopping bag')

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('view_shopping_bag'))


def remove_from_shopping_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        shopping_bag = request.session.get('shopping_bag', {})

        if size:
            del shopping_bag[item_id]['items_by_size'][size]
            if not shopping_bag[item_id]['items_by_size']:
                shopping_bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your shopping bag')
        else:
            shopping_bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your shopping bag')

        request.session['shopping_bag'] = shopping_bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
