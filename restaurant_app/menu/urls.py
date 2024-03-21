from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


#app_name = 'menuapp' -> namespacing

urlpatterns = [
    path("menu", main_menu, name="menu"),
    path("pizzamenu", pizza_menu, name="pizza_menu"),
    path("burgermenu", burger_menu, name="burger_menu"),
    path("sidemenu", side_menu, name="side_menu"),
    path('add_to_cart/<int:product_uuid>/', add_to_cart, name='add_to_cart'),
    path('extras/<str:meal_type>/', extras, name='extras'),
]