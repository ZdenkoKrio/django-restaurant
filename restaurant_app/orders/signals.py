# V orders aplikácii
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

# V orders aplikácii
@receiver(post_save, sender=Order)
def order_status_changed(sender, instance, **kwargs):
    if not kwargs['created'] and 'status' in kwargs['update_fields']:
        # Spracovanie zmeny stavu objednávky
        pass



@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):
    if created:
        # Spustiť proces alebo akciu súvisiacu s novou objednávkou
        # Napríklad, môžete tu vyvolať logiku platobnej brány
        pass



