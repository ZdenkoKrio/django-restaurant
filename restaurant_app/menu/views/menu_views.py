from django.http import HttpResponse
from django.template import loader
from ..models import *
from ..models.enums.MealType import MealTypeChoices


def main_menu(request):
  template = loader.get_template('main_menu.html')
  return HttpResponse(template.render({}, request))


def pizza_menu(request):
  return meal_menu(request, "Pizza", True)


def burger_menu(request):
  return meal_menu(request, "Burger", True)


def side_menu(request):
  return meal_menu(request, "Side", False)


def meal_menu(request, meal_name, has_ingredients):
  meal = eval(f"{meal_name}.{meal_name}.objects.all().values()")
  ingredients = ""

  if has_ingredients:
    ingredients = IngredientModel.Ingredient.objects.filter(
      meal_type=eval(f"MealTypeChoices.{meal_name.upper()}")).values()

  template = loader.get_template('meal_menu.html')

  context = {
    "title": f"{meal_name} Menu",
    'meal': meal,
    "meal_type": meal_name,
    'ingredients': ingredients,
    "has_ingredients": has_ingredients,
  }
  return HttpResponse(template.render(context, request))


def extras(request, meal_type):
  ingredients = IngredientModel.Ingredient.objects.filter(
    meal_type=eval(f"MealTypeChoices.{meal_type.upper()}")).values()

  template = loader.get_template('extras.html')

  context = {
    "meal_type": meal_type,
    'ingredients': ingredients,
  }
  return HttpResponse(template.render(context, request))


def item_detail(request, type, id):
  template = loader.get_template('details.html')

  return HttpResponse(template.render({}, request))

