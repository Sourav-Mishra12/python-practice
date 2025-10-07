
# ENCAPSULATION

#class BadBankAccount:
#    def __init__(self,balance):
 #       self.balance  = balance


#account = BadBankAccount(0.0)
#account.balance = -1
#print(account.balance)

class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property      # getter method
    def balance(self):
        return self._balance
    
    def deposit(self,amount):
        if amount <= 0 :
            raise ValueError("deposit amount must be positive")
        self._balance += amount

    def withdraw(self,amount):
        if amount <= 0 :
            raise ValueError("amount should be positive")
        elif amount >= self._balance:
            raise ValueError("insufficient balance")
        else:
            self._balance -= amount

account = BankAccount()
print(account.balance)
account.deposit(4.99)
print(account.balance)


# ABSTRACTION

# reduce complexity by hiding unnecessary details 

class EmailService:
    def _connect(self):
        print("connect to email server")

    def _authenticate(self ):
        print("Authenticating....")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending the email....")
        self._disconnect

    def _disconnect(self):
        print("disconnecting")


email = EmailService()
email.send_email()


# INHERITANCE 

# INHERITANCE is a fundamental concept in OOP that involves creating new classes (subclass or derived classes) based on existing classes (superclasses or base classes) it is " is a " relatioinship

class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("vehicle is starting")

    def stop(self):
        print("vehicle is stopping")

class Car(Vehicle):
    def __init__(self, brand, model, year,number_of_doors,number_of_wheels):
        super().__init__(brand,model,year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

class Bike(Vehicle):
    def __init__(self, brand, model, year , number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels

car = Car("ford" , "focus" , 2008 , 5 , 4)
bike = Bike("honda" , "schoopy" , 2018 , 2)
print(car.__dict__)
print(bike.__dict__)

car.start()


# POLYMORPHISM 

# the word polymorphism is derived from GREEK and means "having multiple forms"
# POLY : many   ;  MORPH : forms 

