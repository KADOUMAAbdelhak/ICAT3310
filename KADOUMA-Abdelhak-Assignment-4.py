#!/usr/bin/env python3

# Part 1: Comparing x and y
x = 10
y = 11

if x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equal")
else:
    print("y is greater than x")

print("\n") 

# Part 2: Comparing a, b, and c
a = 100
b = 50
c = 200

if a > b and c > a:
    print("a and c are greater than b")

print("\n") 

# Part 3: While loop with i
i = 1
while i < 10:
    print(i)
    i += 1
print("i is no longer less than 10")

print("\n") 

# Part 4: Printing list items with for loop
oses = ["Windows 10", "Windows 11", "macOS", "Linux", "BSD"]
for os in oses:
    print(os)
print("Finished!")

print("\n") 

# Part 5: Comparing oses and oses2
oses2 = ["macOS"]
for os in oses:
    if os in oses2:
        break  # Stop before printing macOS
    print(os)