# Class example
class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def function_name(self, otherargs):
        do something here.

# Object instance example
account = Account("PYTHON/Udemycourse/OOP_practice/balance.txt") 

# Instance variable example
class Example:
    def __init__(self, filepath):
        self.filepath = filepath # <-- the instance variable


# Class variable example
class Example2:

    type = "example" # <-- the class variable
    # shared by all instances in the class

# Doc strings example

class Example3:
    """this is the doc strings example.
    it explains the use of the class.
    if you print the object instance with .__doc__ 
    you can see the doc string
    
    ex.
    example3 = Example3()
    print(example3.__doc__)"""

# Data Member
    # It's essentially a variable within the class

# Constructor
    # the init function

# Methods
    # the functions in the class.

# Inheritance example
class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath) #Access to the Account class
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

