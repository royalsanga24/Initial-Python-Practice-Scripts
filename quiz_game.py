# Python Quiz  

print("Welcome to Python Quiz!")
print("How to play:- You will be asked one questions and each question carries one point. Right answer will add one point to the score. There will be total 5 questions.")
score = 0
answer = input("Question 1: What is the capital of Finland?")
if answer == "Helsinki":
    print("Correct!")
    score = score + 1
else:
    print("Oops, wrong answer.")
        

answer = input("Question 2: Which planet is closest to the sun?")
if answer == "Mercury":
    print("Correct!")
    score = score + 1
else:
    print("Oops, wrong answer.")
        
answer = input("Question 3: Where was the mojito cocktail created?")
if answer == "Cuba":
    print("Correct!")
    score = score + 1
else:
    print("Oops, wrong answer.")
        
answer = input("Question 4: How many sides does a heptadecagon have?")
if answer == "Seventeen":
    print("Correct!")
    score = score + 1
else:
    print("Oops, wrong answer.")
        
answer = input("Question 5: What's a baby rabbit called?")
if answer == "Kit":
    print("Correct!")
    score = score + 1
else:
    print("Oops, wrong answer.")
        
if(score==5):
    print("Congratulations you scored full! Your score is: {} out of 5".format(score))

elif(3<score<=4):
    print("Good job! Your score is: {} out of 5".format(score))

elif(1<=score<=2):
    print("You can do better! Your score is: {} out of 5".format(score))

else:
    print("Oops! Your score is: {} out of 5".format(score))


