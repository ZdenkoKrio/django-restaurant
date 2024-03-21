from django.db import models


class PizzaBaseChoices(models.TextChoices):
    TOMATO = 'TO', 'Tomato Pasta'
    CREAM = 'CR', 'Cream'
    BBQ = "BB", "Barbecue sauce"
