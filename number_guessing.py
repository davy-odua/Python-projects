#NUMBER GUESSING GAME
#Dice rolling

import random

# play = True
# while play:
#     dice = input("Enter the number (y/n): ").lower()
#
#     if dice == "y":
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1,6)
#         print(f"{dice1}, {dice2}")
#
#     elif dice == "n":
#         print("Thank you for playing!")
#         break
#
#     else:
#         print("Invalid choice")





# guessing = True
# while guessing:
#     number = int(input("Enter a number between 1 and 100: "))
#
#     if number > 8:
#         print("Too high!")
#
#     elif number < 8:
#         print("Too low")
#
#     elif number == 8:
#         print("Congratulations! You guessed the number.")
#         break
#
#     else:
#         print("Please enter a valid number")

playing = True
while playing:
    number = int(input("Guess a number between 1 and 100: "))
    correct_no = random.randint(1, 100)

    if number == correct_no:
        print(f"Congratulations! You guessed the correct number")
        break
    elif correct_no > number < 100:
        print(f"Too high!.")
    elif number < correct_no:
        print("Too low!")

    else:
        print("Please enter a valid number: ")


