from django.shortcuts import render

# Create your views here.
def process_payment(request, order_id):
    order = Order.objects.get(id=order_id)
    # Implementujte logiku platby (napr. integrácia s platobnou bránou)
    if payment_successful:
        order.status = Order.PAID
        order.save()
        # Presmerovanie na stránku s potvrdením alebo iné akcie
