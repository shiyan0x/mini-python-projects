class insufficentBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise insufficentBalanceError("insufficent balance in your account")
        self.balance -= amount
        print("withdram succesful")

try:
    acc = BankAccount(2000)
    acc.withdraw(3000)
except insufficentBalanceError as e:
    print("Transection failed", e)
        