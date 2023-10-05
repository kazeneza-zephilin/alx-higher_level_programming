#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
result = add(a, b)
print(f"{a} + {b} = {result}")

result = sub(a,b)
print(f"{a} - {b} = {result}")

result = mul(a,b)
print(f"{a} * {b} = {result}")

result = div(a, b)
print(f"{a} / {b} = {result}")