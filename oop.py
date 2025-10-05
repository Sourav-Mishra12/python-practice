
from datetime import datetime 

class Dog:
    def __init__(self , name , breed , owner): # self keyword is used to point the current instance of the class it gives an object access to its own attributes and methods
            self.name = name
            self.breed = breed
            self.owner = owner


    def bark(self):  # bark function
        print("woof woof")


class Owner:  # owner class
     def __init__(self,name,contact,address):
          self.name = name
          self.phone_number = contact
          self.address = address


owner1 = Owner("sourav" , "2200998877" , "howrah") #  making an instance of the class named Owner
dog1 = Dog("bruce " , "siberian husky" , owner1 ) # making an instance of the class named Dog
print(dog1.owner.name)  # calling the Owner class's attribute which is "name"

owner2 = Owner("srishti" , "5566774488" , "kolkata")
dog2 = Dog("jack" , " alaskan malamut" , owner2)
print(dog2.owner.name)  # same done for another instance



# another class

class Person :
     def __init__(self,name,age):
          self.name = name
          self.age = age 

     def greet(self):
          print(f"hello my name is {self.name} and i am {self.age} years old")


person1 = Person("srishti" , 22)
person1.greet()

person2 = Person("sakshi" , 24)
person2.greet()


# different ways of accessing and modifying data in objects


class User:
     def __init__(self,username,email,password):
          self.username = username
          self.email = email
          self.password = password

     def say_hi_to_user(self,user):
          print(f"Sending message to {user.username} : Hello {user.username} , it's {self.username} ")


user1 = User("srishti" , "varmasrishti99@gmail.com" , "abc")
user2 = User("sourav" , "mishrasourav44@gmail.com" , "123")
user1.say_hi_to_user(user2)

user1 = User("srishti" , "varmasrishti99@gmail.com" , "abc")

print(f"the old email id is : {user1.email}")

user1.email = "varmasrishti66@gmail.com"

print(f"the new email id is : {user1.email}")

# getting and setting the data of an object without this the data can easily be modified

# 1. The traditional way is :  to make the data private and use getters and setters

class User_info:
     def __init__(self,username,email,password):
          self.username = username
          self._email = email # rewriting self.email to self._email to make it protected (prefexing an underscore)
          # and in order to make it private completely just add double underscore in the prefix
          self.password = password

     
     def get_email(self):  # getter method
           print(f"email accessed at :  {datetime.now()}")   
           return self._email
     
     def set_email(self,new_email):
          if "@" in new_email:
           self._email = new_email
          else :
               print("error")
     
user1 = User_info("soumo" , "soumo890@gmail.com" , "hhjji890")
 
print(user1.get_email())

user1.set_email("yrushh@gsnvs")
print(user1.get_email())


# Name mangling in Python is a mechanism that changes the name of class attributes that are prefixed with double underscores (__) to make them harder to access from outside the class. It’s used to avoid naming conflicts in subclasses and enforce a stronger sense of "private" access.
# it is not for true security though 

# the "consenting adults" philosophy

