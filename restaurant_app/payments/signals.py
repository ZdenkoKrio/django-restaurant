# V payments aplikácii
@receiver(payment_successful_signal, sender=Payment)
def payment_successful(sender, order, **kwargs):
    order.status = Order.PAID
    order.save()
    # Ďalšie akcie, ako odoslanie emailu
