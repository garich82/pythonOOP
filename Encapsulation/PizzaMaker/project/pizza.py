from typing import Dict
from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.toppings: Dict[str, float] = {}
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self._name = value

    @property
    def dough(self) -> Dough:
        return self._dough

    @dough.setter
    def dough(self, value: Dough):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self._dough = value

    @property
    def max_number_of_toppings(self) -> int:
        return self._max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value: int):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self._max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")

        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self) -> float:
        total_weight: float = self.dough.weight
        total_weight += sum(self.toppings.values())
        return total_weight
