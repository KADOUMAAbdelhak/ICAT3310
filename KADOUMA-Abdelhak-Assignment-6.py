#!/usr/bin/env python3

# 1. Create x using min() and y using max().
x = min(1, 2, 3)
y = max(5, 10, 15)
print(x)
print(y)

# 2. Create z with abs() function and print.
z = abs(-5.00)
print(z)

# 3. Create a with pow(2,3) and print.
a = pow(2, 3)
print(a)

# 4. Import math and use sqrt, ceil, floor, pi.
import math

b = math.sqrt(256)
print(b)

c = math.ceil(1.5)
d = math.floor(2.5)
print(c)
print(d)

e = math.pi
print(e)

# 5. Parse JSON and print values.
import json

f = '{ "name":"John Doe", "age":50, "city":"Vaasa" }'
parsed_f = json.loads(f)
print(parsed_f["name"])
print(parsed_f["age"])
print(parsed_f["city"])

# 6. Convert a Python dict to JSON and print.
h = { "name": "John Doe", "age": 50, "city": "Vaasa" }
i = json.dumps(h)
print(i)

# 7. Import re, use findall, search, split, sub.
import re

txt = "Python for Systems Intelligence and Analytics"
j = re.findall("Python", txt)
print(j)

k = re.search("Python", txt)
print(k)

l = re.split(r"\s", txt)
print(l)

m = re.sub(r"\s", "0", txt)
print(m)

# 8. Try/Except/Finally block.
try:
    print(n)  # This will trigger an exception because n is not defined.
except:
    print("An exception occurred")
finally:
    print("The Try Except is finished")
