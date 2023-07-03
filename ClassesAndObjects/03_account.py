class Account:
    def __init__(self, id, name, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


# Create an account with id=1, name="John Doe", and initial balance of 1000
account = Account(1, "John Doe", 1000)

# Credit 500 to the account
account.credit(500)

# Debit 200 from the account
account.debit(200)

# Get account information
print(account.info())
