class BankAccount :
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance

    def deposit(self, amount):
        if amount >0:
            self.balance += amount
        else:
            self.balance -= amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("insufficent balance")
    
    def get_balance(self):
        return self.balance

a1 = BankAccount("Shivam", 10000)
print("1st" , a1.get_balance())
a1.deposit(5000)
a1.withdraw(8000)
print("final amount", a1.get_balance())



