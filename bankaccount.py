class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        """ insert function to check if money are real not fake """
        self.balance += amount

    def withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount

    def __str__(self):
        return str(self.balance)
