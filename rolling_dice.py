#Create a dice which prints random numbers.
#1. Question - Enter the number (y or n)
#when we enter y we should generate the random numbers
#Loop when you enter y
#2. When we enter n we should print (Thanks) and terminate
#when we enter another string which is not mentioned then print(Invalid choice)
#loop when you enter an invalid choice.


import random

dicing = False
while not dicing:
    dice = input("Enter the number? (y/n): ").lower()
    if dice == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"({dice1}, {dice2})")
    elif dice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice")
















