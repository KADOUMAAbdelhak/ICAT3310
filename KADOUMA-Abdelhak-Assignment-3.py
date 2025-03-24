#!/usr/bin/env python3

# This is KADOUMA Abdelhak and this my python assignment 3

print("\n") 

# Print arithmetic operations
print(1 + 1)  # Addition
print(1 - 1)  # Subtraction
print(1 * 1)  # Multiplication
print(1 / 1)  # Division

print("\n") 

# Create a list called myfirstlist with values 1, 2, 3, 4, and 5
myfirstlist = [1, 2, 3, 4, 5]

# Print the entire list to the screen
print(myfirstlist)

print("\n") 

# Print each value of the list individually
for value in myfirstlist:
    print(value)

print("\n") 

# Sort the list in reverse order and print the reversed list
myfirstlist.reverse()
print(myfirstlist)

print("\n") 

# Print each value of the reversed list individually
myfirstlist.reverse() # back to original
for value in myfirstlist:
    print(value)

print("\n") 

# Create tuple called myfirsttuple that contains values: my last name = KADOUMA, my age = 25, True and float 1.5.
myfirsttuple = ("KADOUMA", 25, True, 1.5)

# Print the tuple to the screen
print(myfirsttuple)

print("\n") 

# Create three sets with specified values
set1 = {"one", "two", "three"} # Set1 contains values: one, two and three.
set2 = {1, 2, 3} # Set2 contains values 1,2 and 3.
set3 = {False, True} # Set3 contains values true and false.

# Print all three sets to the screen
print(set1)
print(set2)
print(set3)

print("\n") 

# Create dictionary that contains 3 keys: Course, language and year with values: Python for Systems Intelligence and Analytics, Python and 2025.
mydictionary = {
    "Course": "Python for Systems Intelligence and Analytics",
    "Language": "Python",
    "Year": 2025
}

# Print the dictionary to the screen
print(mydictionary)