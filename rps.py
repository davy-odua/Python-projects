#Rock, Paper, Scissors
#  ,🪨, 📄 ,✂️

import random

#BY CONVENTION WE DECLARE CONSTANTS USING UPPER_CASE LETTERS
ROCK = "R"
PAPER = "P"
SCISSORS = "S"

emojis = {ROCK : "🪨" , PAPER: "📄" , SCISSORS: "✂️" }
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Enter rock ,paper or scissors (R,P,S): ").upper()
        if user_choice  in choices:
            return user_choice
        else:
            print("Invalid choice!")

def display_choices(user_choice, comp_choice):
    print(f"You chose {emojis[user_choice ]}")
    print(f"Computer chose {emojis[comp_choice ]}")

def determine_winner(user_choice, comp_choice):

    if user_choice  == comp_choice:
        print("Tie")

    elif(
        (user_choice  == PAPER and comp_choice == ROCK) or
        (user_choice  == SCISSORS and comp_choice == PAPER) or
        (user_choice  == ROCK and comp_choice == SCISSORS )):
        print("You win")

    else:
        print("You lose")

def play_game():
    while True:
        user_choice = get_user_choice()

        comp_choice = random.choice(choices)

        display_choices(user_choice, comp_choice)

        determine_winner(user_choice, comp_choice)

        cont = input("Do you want to continue? (y/n): ").lower()
        if cont == "n":
            break

play_game()


#DRY
#REFACTORING = Changing the structure of our code without changing its functionality
# COMMON REFACTORING TECHNIQUE (MODULARIZATION)
# Modularization = Breaking down a large program into smaller
#                  reusable parts called modules or functions





