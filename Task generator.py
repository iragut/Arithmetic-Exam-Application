import random

symbol = ['-', '+', '*']
number = [2, 3, 4, 5, 6, 7, 8, 9]
a = random.choice(number)
s = random.choice(symbol)
b = random.choice(number)
if s == "+":
    print(f"{a} + {b}")
    answer = a + b
elif s == "-":
    print(f"{a} - {b}")
    answer = a - b
else:
    print(f"{a} * {b}")
    answer = a * b
index = int(input())
if index == answer:
    print("Right!")
else:
    print("Wrong!")
