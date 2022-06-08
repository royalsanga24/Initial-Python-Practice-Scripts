import random
import time

print("Welcome to Python's Rock, Paper and Scissor Game!")
print("Rules: There will be total 3 attempts. If you score 2 or more points, you win.")
CHOICES = ["Rock" , "Paper", "Scissor"]
# print(COMPUTER)
start = input("Do you wish to start? Y or N-")
score = 0
if(start == "Y"):
    for i in range(0, 3):
        COMPUTER = random.choice(CHOICES)
        usr_input = input("Enter your choice in 3..:- ")
        time.sleep(2)
        print("Enter your choice in 2..")
        time.sleep(1)
        print("Enter your choice in 1..")
        time.sleep(1)
        if usr_input:
            if (COMPUTER == "Rock" and usr_input == "Paper"):
                print("Computer chose {}".format(COMPUTER))
                print("You Won")
                score += 1
            elif (COMPUTER == "Rock" and usr_input == "Scissor"):
                print("Computer chose {}".format(COMPUTER))
                print("You Lost")
            elif (COMPUTER == "Paper" and usr_input == "Rock"):
                print("Computer chose {}".format(COMPUTER))
                print("You Lost")
            elif (COMPUTER == "Paper" and usr_input == "Scissor"):
                print("Computer chose {}".format(COMPUTER))
                print("You Won")
                score += 1
            elif (COMPUTER == "Scissor" and usr_input == "Rock"):
                print("Computer chose {}".format(COMPUTER))
                print("You Won")
                score += 1
            elif (COMPUTER == "Scissor" and usr_input == "Paper"):
                print("Computer chose {}".format(COMPUTER))
                print("You Lost")
            else:
                print("Computer chose {}".format(COMPUTER))
                print("Both are same. Try Again.")
        else:
            print("Computer chose {}".format(COMPUTER))
elif(start == "N"):
    exit()

# print(score)
if 2 <= score:
    print("Congratulations! You won. Your score is {}".format(score))
elif score < 2:
    print("OOPS! Better luck next time. Your score is {}".format(score))