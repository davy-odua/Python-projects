#NUMBER GUESSING GAME
#Dice rolling

import random

rand = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > rand:
            print("Too high!")
        elif guess < rand:
            print("Too low")
        else:
            print("Congratulations, You found the correct number.")
            break
    except ValueError:
        print("Please enter a valid number")










