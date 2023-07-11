from typing import List
from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription

class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int) -> str:
        subscription = next((sub for sub in self.subscriptions if sub.id == subscription_id), None)
        if subscription:
            customer = next((cust for cust in self.customers if cust.id == subscription.customer_id), None)
            trainer = next((trn for trn in self.trainers if trn.id == subscription.trainer_id), None)
            plan = next((pln for pln in self.plans if pln.id == subscription.exercise_id), None)
            equipment = None
            if plan:
                equipment = next((eqp for eqp in self.equipment if eqp.id == plan.equipment_id), None)

            if customer and trainer and equipment and plan:
                info = f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
                return info

        return "Subscription not found"
