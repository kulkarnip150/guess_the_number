import random


def driver():
    print(
        """
           1: Guess the number between 1 and 50
           2: Guess the number between 1 and 100
           3: Guess the number between -100 and 100
           4: Guess the number between -1000 and 1000
           5: Exit"""
    )
    ch = int(input())
    if ch == 1:
        novice()
    elif ch == 2:
        rookie()
    elif ch == 3:
        legend()
    elif ch == 4:
        ultra_legend()
    else:
        exit(0)


def novice():
    num = int(input(" Guess the number between 1 and 50 "))
    ran_num = random.randrange(1, 50)
    working(num, ran_num)


def rookie():
    num = int(input(" Guess the number between 1 and 100 "))
    ran_num = random.randrange(-100, 100)
    working(num, ran_num)


def legend():
    num = int(input(" Guess the number between -100 and 100 "))
    ran_num = random.randrange(1, 100)
    working(num, ran_num)


def ultra_legend():
    num = int(input(" Guess the number between -1000 and 1000 "))
    ran_num = random.randrange(-100, 100)
    working(num, ran_num)


def working(num, ran_num):
    count = 0
    while ran_num != num:
        if ran_num < num:
            print(" You need to guess lower, Try again ")
            num = int(input(" Enter number less than {}: ".format(num)))
            count = count + 1
        elif ran_num > num:
            print(" You need to guess higher, Try again")
            num = int(input(" Enter number more than {}: ".format(num)))
            count = count + 1
        else:
            break
    print()
    print(" You guessed right number !!!")
    print(" You take {} chance to guess right number ".format(count))


driver()
