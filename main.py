from typing import List


class Shop:
    def __init__(self, name: str, items: List[str]):
        self.name = name
        self.items = items

    def get_items_count(self) -> int:
        return len(self.items)


my_shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
billa = Shop("Billa", ["Billa yogurt", "Billa meat"])

print(billa.get_items_count())