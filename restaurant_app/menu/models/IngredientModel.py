from django.db import models
from .enums.MealType import MealTypeChoices


class Ingredient(models.Model):
    # pre studijne ucely použijeme variantu type-id
    #uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # in grams
    price = models.DecimalField(max_digits=6, decimal_places=2)
    meal_type = models.CharField(max_length=2, choices=MealTypeChoices.choices, default=MealTypeChoices.PIZZA)

    def __str__(self):
        return f"{self.name} - {self.weight}g     {self.price},- Czk"
