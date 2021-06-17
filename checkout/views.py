from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Gt8XQFmBm2bmmS2xNYdTwa5Pecl3joaQFpb4xkuVTzGHcgkeYEcoXLjT64fZxzdPDD12uHOZz2odZahmtH7QjO500pSckCSsU',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
