# Number Guessing Game using Python

import random

print("Welcome to the Number Guessing Game \n")
print("I'm thinking a number between 1 and 100 \n")

number = random.randint(1, 100)
print(f"Hint {number}")


def guess():
    guess = int(input("Make a guess: "))
    if guess != number:
        if guess > number:
            print("Too high. \n")
        else:
            print("Too low. \n")
        return ("Guess Again \n")
    else:
        print("You guessed it! You won! \n")


def easy_attempts():
    i = 10
    while i > 0:
        print(f"You have {i} attempts remaining to guess the number. \n")
        guess()
        i = i-1
    print("You've run out of guesses, you lose. \n")


def hard_attempts():
    i = 5
    for i in range(1, 5, 1):
        print(f"You have {i} attempts remaining to guess the number. \n")
        guess()
        i -= 1
    print("You've run out of guesses, you lose. \n")


ask = input("Choose a difficulty. Type 'easy' or 'hard': ")
if ask == "easy":
    print(easy_attempts())
else:
    print(hard_attempts())
