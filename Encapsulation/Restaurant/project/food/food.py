from project.product import Product


class Food(Product):
    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price)
        self.__grams = grams

    @property
    def grams(self) -> int:
        return self.__grams

    def get_grams(self) -> float:
        return self.__grams