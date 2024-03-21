from django.shortcuts import render

# Create your views here.
def create_order(request):
    cart = request.session.get('cart', {})
    if not cart:
        # Chyba alebo správa, že košík je prázdny
        return

    order = Order.objects.create(user=request.user)  # Pridajte potrebné informácie
    for item_id, quantity in cart.items():
        menu_item = MenuItem.objects.get(id=item_id)
        OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)

    # Vyčistenie košíka
    request.session['cart'] = {}
    # Presmerovanie na platbu alebo potvrdenie objednávky
