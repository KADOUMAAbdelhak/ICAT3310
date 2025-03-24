#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Print Matplotlib Version
print(f"Matplotlib version: {matplotlib.__version__}")

# Pyplot Line Plot
plt.figure()
x = np.linspace(1, 10, 10)
y = x * 10
plt.plot(x, y)
plt.savefig("KADOUMA-Abdelhak-Pyplot.png")
plt.close()

# Multiple Points
plt.figure()
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.plot(x, y)
plt.savefig("KADOUMA-Abdelhak-Multi-Points.png")
plt.close()

# Markers
plt.figure()
plt.plot(x, y, marker='o')
plt.savefig("KADOUMA-Abdelhak-Markers.png")
plt.close()

# Line Style and Color
plt.figure()
plt.plot(x, y, linestyle='dotted', color='red', marker='o')
plt.savefig("KADOUMA-Abdelhak-Linestyle-and-Color.png")
plt.close()

# Labels
plt.figure()
plt.plot(x, y)
plt.xlabel("Year")
plt.ylabel("Price")
plt.savefig("KADOUMA-Abdelhak-Labels.png")
plt.close()

# Grid
plt.figure()
plt.plot(x, y)
plt.xlabel("Year")
plt.ylabel("Price")
plt.title("Apple Watch Data")
plt.grid()
plt.savefig("KADOUMA-Abdelhak-Grid.png")
plt.close()

# Subplots
fig, axs = plt.subplots(1, 2)
axs[0].plot(x[:5], y[:5])
axs[1].plot(x, y)
plt.savefig("KADOUMA-Abdelhak-Subplot.png")
plt.close()

# Scatter and Different Colors
plt.figure()
colors = np.random.rand(len(x))
plt.scatter(x, y, c=colors)
plt.savefig("KADOUMA-Abdelhak-Scatter-Color-Each-Dot.png")
plt.close()

# Bars
plt.figure()
languages = ["Python", "Ruby", "Java", "C++"]
values = [10, 9, 8, 7]
plt.bar(languages, values)
plt.savefig("KADOUMA-Abdelhak-Bars.png")
plt.close()

# Histogram
plt.figure()
data = np.random.normal(170, 10, 250)
plt.hist(data, bins=10)
plt.savefig("KADOUMA-Abdelhak-Histogram.png")
plt.close()

# Pie Chart
plt.figure()
plt.pie(values, labels=languages, autopct='%1.1f%%')
plt.savefig("KADOUMA-Abdelhak-Pie.png")
plt.close()
