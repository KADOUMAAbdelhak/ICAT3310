#!/usr/bin/env python3
import os

# Read demofile.txt and print everything
with open("demofile.txt", "r") as file:
    content = file.read()
    print(content)

# Read first 6 letters from demofile.txt
with open("demofile.txt", "r") as file:
    first_six = file.read(6)
    print(first_six)

# Read last two lines from demofile.txt
with open("demofile.txt", "r") as file:
    lines = file.readlines()
    last_two = "".join(lines[-2:])
    print(last_two)

# Read first two lines from demofile.txt and close file
with open("demofile.txt", "r") as file:
    first_two = "".join(lines[:2])
    print(first_two)

# Create demofile2.txt and add text
with open("demofile2.txt", "w") as file:
    file.write("This is my demofile2.txt")

# Read and print demofile2.txt
with open("demofile2.txt", "r") as file:
    print(file.read())

# Copy demofile2.txt to demofile3.txt
with open("demofile2.txt", "r") as file:
    data = file.read()
with open("demofile3.txt", "w") as file:
    file.write(data)

# Overwrite demofile3.txt with new text
with open("demofile3.txt", "w") as file:
    file.write("This is my demofile3.txt")

# Read and print demofile3.txt
with open("demofile3.txt", "r") as file:
    print(file.read())

# Remove demofile2.txt
os.remove("demofile2.txt")
