from project.product import Product


class Drink(Product):
    def __init__(self, product_name):
        super().__init__(product_name, 10)
        self.product_name = product_name
