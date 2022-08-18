import random

def isnum(num):
    try:
        int(num)
        return False
    except ValueError:
        return True


symbol = ['-', '+', '*']
number = [2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
n = 0
while counter < 5:
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
    while True:
        index = input()
        if isnum(index):
            print("Incorrect format.")
        else:
            if int(index) == answer:
                print("Right!")
                counter += 1
                n += 1
                break
            else:
                print("Wrong!")
                counter += 1
                break
print(f"Your mark is {n}/5.")