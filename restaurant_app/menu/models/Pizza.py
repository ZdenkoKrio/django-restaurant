from django.db import models
from django.db.models import Sum
from .IngredientModel import Ingredient
from .enums.PizzaBase import PizzaBaseChoices
from restaurant_app.config import BASE_PIZZA_PRICE, PIZZA_DOUGH_WEIGHT
import uuid


class Pizza(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    base = models.CharField(max_length=2, choices=PizzaBaseChoices.choices, default=PizzaBaseChoices.TOMATO)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        pizza_base = dict(PizzaBaseChoices.choices).get(str(self.base), 'ERROR_BASE')
        return f"""
    {self.name}
    Ingrediencie: {pizza_base}, {self.__get_ingredients_list()}
    Váha: {self.total_weight}       Cena: {self.total_price}
"""

    @property
    def total_weight(self):
        ingredients = self.ingredients.aggregate(total_weight=Sum('weight'))
        return PIZZA_DOUGH_WEIGHT + ingredients['total_weight']

    @property
    def total_price(self):
        ingredients = self.ingredients.aggregate(total_price=Sum('price'),
                                                 output_field=models.DecimalField())
        return BASE_PIZZA_PRICE + ingredients['total_price']

    def __get_ingredients_list(self):
        return ', '.join([ingredient.name for ingredient in self.ingredients.all()])

