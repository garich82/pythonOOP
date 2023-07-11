from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity() and customer not in self.customers:
            self.customers.append(customer)
            return True
        return False

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)
            return True
        return False

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self._find_customer_by_id(customer_id)
        dvd = self._find_dvd_by_id(dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        if not customer or not dvd:
            return "Customer or DVD not found"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = self._find_customer_by_id(customer_id)
        dvd = self._find_dvd_by_id(dvd_id)

        if not customer or not dvd:
            return "Customer or DVD not found"

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        customers_repr = "\n".join([repr(customer) for customer in self.customers])
        dvds_repr = "\n".join([repr(dvd) for dvd in self.dvds])
        return f"{customers_repr}\n{dvds_repr}"

    def _find_customer_by_id(self, customer_id: int):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None

    def _find_dvd_by_id(self, dvd_id: int):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd
        return None
