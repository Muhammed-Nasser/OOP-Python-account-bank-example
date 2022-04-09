class Account():
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def __str__(self):
        return (f"{self.name}")
    
    def deposite(self, amount):
        self.balance += amount
        print(f"You added {amount} to your balance! Total balance {self.balance}")
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"withdraw Success! Total balance {self.balance}")
        else:
            print("Sorry, You don't have enough money!")
            
            
ahmed = Account("Ahmed Mohamed")
print(ahmed)
print(ahmed.balance)
ahmed.deposite(5000)
print(ahmed.balance)
ahmed.withdraw(5000)
print(ahmed.balance)
ahmed.withdraw(1000)
print(ahmed.balance)