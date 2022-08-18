calculator = input().split()
if calculator[1] == "+":
    print(int(calculator[0]) + int(calculator[2]))
elif calculator[1] == "-":
    print(int(calculator[0]) - int(calculator[2]))
elif calculator[1] == "*":
    print(int(calculator[0]) * int(calculator[2]))