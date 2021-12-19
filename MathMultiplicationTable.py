import time
import random

exit = True
correctAnswers = 0
questions = 0

def CheckAnswer(answer, userAnswer):
    if (userAnswer == "quit"):
        return -1
    elif (answer == int(userAnswer)):
        return 1
    else:
        return 0
        


def CreateQuestion(x,y):
    userAnswer = input("\nWhat is the answer to: " + str(x) + " * " + str(y) + ": \n")
    return CheckAnswer(x*y, userAnswer)

print("What dimensions do you want your times table?")
range = input("1st dimension: ")
range2 = input("2nd dimension: ")
print("Enter quit if you are done.")
while exit == True:
    num1 = int(range)
    num2 = int(range2)
    userAnswer = CreateQuestion(random.randint(0,num1),random.randint(0,num2))
    if userAnswer == -1:
        exit = False
    else:
        correctAnswers += userAnswer
        questions += 1
print("You got " + str(correctAnswers) + " question correct out of " + str(questions) + "\n")