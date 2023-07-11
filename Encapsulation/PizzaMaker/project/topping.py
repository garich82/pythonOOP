class Topping:
    def __init__(self, topping_type, weight):
        self._topping_type = None
        self._weight = None
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self._topping_type

    @topping_type.setter
    def topping_type(self, value):
        if not value:
            raise ValueError("The topping type cannot be an empty string")
        self._topping_type = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self._weight = value
