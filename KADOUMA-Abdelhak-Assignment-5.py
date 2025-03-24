#!/usr/bin/env python3

# First function that prints a simple message
def myfirstfunction():
    """This function prints a message to demonstrate basic function creation"""
    print("This is my first function in assignment 5")

# Second function that takes a firstname parameter and adds 'Doe' to it
def mysecondfunction(firstname):
    """This function takes a firstname and prints it with 'Doe' appended"""
    print(firstname + " Doe")

# Person class definition with constructor and method to print name and age
class Person:
    """Class to represent a person with name and age attributes"""
    
    def __init__(self, name, age):
        """Constructor to initialize name and age attributes"""
        self.name = name
        self.age = age
    
    def printnameage(self):
        """Method to print the person's name and age"""
        print(self.name, self.age)

# Call the first function to display the message
myfirstfunction()

# Print a blank line for formatting
print()

# Call the second function twice with different names
mysecondfunction("John")
mysecondfunction("Jane")

# Print a blank line for formatting
print()

# Create two Person objects with name and age
p1 = Person("John", 50)
p2 = Person("Jane", 50)

# Print individual name and age values for each person
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

# Print a blank line for formatting
print()

# Call printnameage method for both Person objects
p1.printnameage()
p2.printnameage()