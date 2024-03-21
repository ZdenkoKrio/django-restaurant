from enum import Enum


class Toppings(Enum):
    TOMATO_BASE = "rajčinovy zaklad"
    CHEESE = "syr"
    CHAMPIONS = "šampiony"
    SALAMI = "salama"
    CORN = "kukurica"
    OLIVES = "olivy"
    BACON = "bacon"

    @staticmethod
    def get_topping_by_num(num):
        for index, member in enumerate(Toppings, start=1):
            if index == num:
                return member
