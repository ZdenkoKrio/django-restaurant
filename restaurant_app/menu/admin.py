from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Burger.Burger)
admin.site.register(Pizza.Pizza)
admin.site.register(IngredientModel.Ingredient)
admin.site.register(Side.Side)
