import random


def isint(num):  # check if num is a integer
    try:
        int(num)
        return False
    except ValueError:
        return True


symbol = ['-', '+', '*']
number = [2, 3, 4, 5, 6, 7, 8, 9]
number_for_square = list(range(11, 30))
counter = 0
n = 0
while True:
    level = input('''Which level do you want? Enter a number: 
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n''')         # select the level
    if level == "1":
        while counter < 5:
            a = random.choice(number)     # block lvl 1,simple operations
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
                if isint(index):
                    print("Wrong format! Try again.")
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
        break
    elif level == "2":     # block lvl 2,squares
        while counter < 5:
            a = random.choice(number_for_square)
            answer = a * a
            print(a)
            while True:
                index = input()
                if isint(index):
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
        break
    else:
        print("Incorrect format.")
save = input(f"Your mark is {n}/5. Would you like to save the result? Enter yes or no.\n")  # if you want to save the result in a file
if save in ['yes', 'y', 'YES', 'Yes']:
    name = input("What is your name?\n")
    save_file = open("results.txt", "a")
    if level == "1":
        save_file.write(f"{name}: {n}/5 in level 1 (simple operations with numbers 2-9).")
        save_file.close()
        print("The results are saved in \"results.txt\".")
    else:
        save_file.write(f"{name}: {n}/5 in level 2 (integral squares of 11-29).")
        save_file.close()
        print("The results are saved in \"results.txt\".")
