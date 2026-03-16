#Roll the dice.
import random

while True:
    dice = input("Roll the dice? (y/n): ").lower()
    if dice == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(dice1, dice2)
    elif dice == "n":
        print(f"Thanks for playing!")
        break
    else:
        print("Invalid choice!")










