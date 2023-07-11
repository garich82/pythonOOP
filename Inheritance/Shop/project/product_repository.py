from typing import List, Union
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> Union[Product, None]:
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def remove(self, product_name: str) -> None:
        for product in self.products:
            if product.product_name == product_name:
                self.products.remove(product)

    def __repr__(self):
        return '\n'.join([f"{product.product_name}: {product.quantity}" for product in self.products])

