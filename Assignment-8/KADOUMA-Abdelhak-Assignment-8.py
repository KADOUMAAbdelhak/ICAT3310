#!/usr/bin/env python3

import mymodule           # Our custom module
import platform           # Built-in module
import numpy as np        # For random numbers
import pandas as pd       # For DataFrame and CSV
from scipy import constants  # For time-unit constants
import matplotlib.pyplot as plt  # For plotting

# 1. Print greetings and person dictionaries
mymodule.greeting(mymodule.person1["name"])
print(f"Name: {mymodule.person1['name']}")
print(f"Age: {mymodule.person1['age']}")
print(f"Country: {mymodule.person1['country']}\n")

mymodule.greeting(mymodule.person2["name"])
print(f"Name: {mymodule.person2['name']}")
print(f"Age: {mymodule.person2['age']}")
print(f"Country: {mymodule.person2['country']}\n")

# 2. Print platform name
print("Platform:", platform.system(), "\n")

# 3. Generate and print a random number using NumPy
random_number = np.random.randint(0, 1001)
print(f"My random number is: {random_number} \n")

# 4. Load visitor_statistics.csv into a DataFrame and print
df = pd.read_csv("visitor_statistics.csv")   # Ensure visitor_statistics.csv is in same folder
print(df, "\n")

# 5. Print time units in seconds using SciPy constants
print("Units in seconds:")
print("Minute:", constants.minute)
print("Hour:", constants.hour)
print("Day:", constants.day)
print("Week:", constants.week)
print("Year:", constants.year, "\n")

# 6. Plot the visitor_statistics.csv data
#    Assume CSV has a column named 'All visitors' you wish to plot against the index
df.plot(y='All visitors', label='All visitors')
plt.title("Monthly Visitors")
plt.xlabel("Month Index (0-11)")
plt.ylabel("Number of Visitors")
plt.show()
