from django.db import models
from django.db.models import Sum
from .IngredientModel import Ingredient
from restaurant_app.config import BASE_BURGER_WEIGHT, BASE_BURGER_PRICE
import uuid


class Burger(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return f"""
    {self.name}
    Ingrediencie: {self.__get_ingredients_list()}
    Váha: {self.total_weight}       Cena: {self.total_price}
"""

    @property
    def total_weight(self):
        ingredients = self.ingredients.aggregate(total_weight=Sum('weight'))
        return BASE_BURGER_WEIGHT + ingredients['total_weight']

    @property
    def total_price(self):
        ingredients = self.ingredients.aggregate(total_price=Sum('price'),
                                                 output_field=models.DecimalField())
        return BASE_BURGER_PRICE + ingredients['total_price']

    def __get_ingredients_list(self):
        return ', '.join([ingredient.name for ingredient in self.ingredients.all()])

