from django.db import models
import uuid

class Side(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # in grams
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"""
    {self.name}
    Váha: {self.weight}       Cena: {self.price}
"""


