class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    @property
    def name(self) -> str:
        return self.__name

    def get_name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    def get_price(self) -> float:
        return self.__price

