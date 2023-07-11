from project.product import Product


class Food(Product):
    def __init__(self, product_name):
        super().__init__(product_name, 15)
        self.product_name = product_name