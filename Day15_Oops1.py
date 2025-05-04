 # Object Oriented Programming Practice
"""These  four are the pillars of OOPs:
1. Encapsulation: Hiding data (using public, protected and private) inside a class.
2. Inheritance: Reusing code using parent-child relationship.
3. Polymorphism: Same method, different behaviour depending on object.
4. Abstraction: Hiding Complex implementation, showing only essentials.
"""

# Bank Account System

# Base class (Encapsulation)
class Account:

    def __init__(self, owner, balance):
        self.owner = owner  # public attribute
        self.__balance = balance # private attribute

    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
            print(f"{amount} deposited. New Balance: {self.__balance}")
        else:
            print("invalid deposit amount")

    def withdraw(self,amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount")

    def get_balance(self):
        return self.__balance
    

if __name__ == "__main__":
    acc = Account("Sumit",250.00)
    print(acc)
    print(acc.owner)
    print(acc.get_balance())  
    print('-' * 60)
    acc.deposit(500.00)
    print(acc.get_balance())
    acc.withdraw(600.00)
    print('-' * 60)
    







