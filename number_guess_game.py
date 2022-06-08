import random

print("Welcome to number guess game! You will have to guess a number in minimum number of chances.")
upper_limit = int(input("What should be the limit:-"))
number = random.randrange(0, upper_limit)
chances = 0
while True:
    chances += 1
    usr_num = int(input("Enter Number:-"))
    if (usr_num < number):
        print("The number is greater than the entered number.")
        continue;

    elif(usr_num > number):
        print("The number is lesser than the entered number.")
        continue;

    elif(usr_num == number):
        print("Your guess is right!")
        print("You guessed in {} chances".format(chances))
        break;