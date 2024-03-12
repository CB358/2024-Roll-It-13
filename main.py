# checks players enter yes (y) or no(n)
import random


def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users dont enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes or no")


def how_to_play():
    print("Welcome to the Math quiz")

    print('''
    
**** How to play ****
To play this math quiz, all you have to do is just answer how many questions you want that you choose the most questions you may have is 10.
You will be able to chose how many you would like soon. 
The questions you are allowed to use are PLUS, MINUS. 
At the end of the questions the computer will show you how many you got right, and which ones you got right.
Those questions you have got right will go to a score out of 10 and the amount of numbers you have will turn into a percentage.
For e.g. a score of 4 your percentage will be 40% out of 100%.
Then the quiz will ask you if you would like to play again.

    ''')


def question():
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    operator = random.randint(1,2)
    # Adding
    if operator == 1:
        answer = num1 + num2
        if int(input(f"{num1} + {num2} =")) == answer:
            print("Correct")
        else:
            print("You are wrong")
    # Subtracting
    elif operator == 2:
        answer = num1 - num2
        if int(input(f"{num1} - {num2} =")) == answer:
            print("Correct")
        else:
            print("You are wrong")

# Main routine

# Loop until true
while True:
    name = input("what is your name?")
    # Check name
    if name != "":
        break
    print("Please enter a username")

print("Welcome " + name + "!")

yesNoAnswer = yes_no(f"Would you like to see the instructions {name}? ")

if yesNoAnswer == "yes":
    how_to_play()

# Player inputs number of questions
# Loop until true
while True:
    numQuestions = int(input("How many questions would you like? "))
    # Check number
    if numQuestions <= 10 and numQuestions >= 1:
        break
    print("Please enter a number between 1 and 10")

# Loop through questions
for x in range(numQuestions):
    print(f"{x + 1}")
    question()
