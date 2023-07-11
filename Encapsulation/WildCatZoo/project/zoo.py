from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if len(self.animals) < self.__animal_capacity:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {type(animal).__name__} added to the zoo"
            else:
                return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = sum(worker.salary for worker in self.workers)
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        needed_amount = sum([a.money_for_care for a in self.animals])
        if self.__budget >= needed_amount:
            self.__budget -= needed_amount
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        animal_counts = {}
        for animal in self.animals:
            animal_type = type(animal).__name__
            if animal_type not in animal_counts:
                animal_counts[animal_type] = 1
            else:
                animal_counts[animal_type] += 1

        animal_status = f"You have {len(self.animals)} animal{'s' if len(self.animals) != 1 else ''}\n"
        for index, (animal_type, count) in enumerate(animal_counts.items()):
            animal_status += f"----- {count} {animal_type}s:\n"
            animal_status += "\n".join(str(animal) for animal in self.animals if type(animal).__name__ == animal_type)
            if index < len(animal_counts) - 1:
                animal_status += "\n"

        return animal_status

    def workers_status(self) -> str:
        worker_counts = {}
        for worker in self.workers:
            worker_type = type(worker).__name__
            if worker_type not in worker_counts:
                worker_counts[worker_type] = 1
            else:
                worker_counts[worker_type] += 1

        worker_status = f"You have {len(self.workers)} worker{'s' if len(self.workers) != 1 else ''}\n"

        # Define the order of worker types
        worker_types = ['Keeper', 'Caretaker', 'Vet']

        # Iterate over the worker types in the desired order
        for index, worker_type in enumerate(worker_types):
            if worker_type in worker_counts:
                count = worker_counts[worker_type]
                worker_status += f"----- {count} {worker_type}s:\n"
                worker_status += "\n".join(
                    str(worker) for worker in self.workers if type(worker).__name__ == worker_type)

                # Check if there are more worker types or if there are workers left to print
                if (index < len(worker_types) - 1) or (index == len(worker_types) - 1 and any(
                        worker_type in worker_counts for worker_type in worker_types[index + 1:])):
                    worker_status += "\n"

        return worker_status
