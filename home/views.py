from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def returns(request):
    """ A view to return the return page """

    return render(request, 'home/return.html')


def delivery(request):
    """ A view to return the delivery page """

    return render(request, 'home/delivery.html')


def contact(request):
    """View handle contact form requests"""

    return render(request, 'home/contact.html')
