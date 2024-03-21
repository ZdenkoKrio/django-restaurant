from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme


def add_to_cart(request, product_uuid):
    next_url = request.POST.get('next', reverse('default_view'))

    if not url_has_allowed_host_and_scheme(next_url, allowed_hosts=request.get_host()):
        return redirect('menu')

    cart = request.session.get('cart', {})
    cart[product_uuid] = cart.get(product_uuid, 0) + 1
    request.session['cart'] = cart
    messages.success(request, 'Položka bola pridaná do košíka!')
    if next_url in ["pizza", "burger"]:
        return reverse('extras', args=[next_url])

    return redirect(f"{next_url}_menu")
