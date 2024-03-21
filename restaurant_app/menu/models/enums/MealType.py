from django.db import models


class MealTypeChoices(models.TextChoices):
    PIZZA = 'PI', 'Pizza'
    BURGER = 'BU', 'Burger'
