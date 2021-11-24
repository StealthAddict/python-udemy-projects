# Class example
class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
        
    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance)) 

# Inheritance example
class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath) #Access to the Account class
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

checking = Checking("PYTHON/Udemycourse/OOP_practice/balance.txt", 1)
print(checking.fee)
checking.transfer(10)
checking.deposit(10)
print(checking.balance)