#Rock, Paper, Scissors

import random

choices = ("R", "P", "S")
while True:
    my_choice = input("Enter rock ,paper or scissors (R,P,S): ").upper()
    if my_choice not in choices:
        print("Invalid choice!")
    else:
        comp_choice = random.choice(choices)
        print(f"You chose {my_choice}")
        print(f"Computer chose {comp_choice}")
        if comp_choice == my_choice:
            print("Tie")
            cont = input("Do you want to continue? (y/n): ").lower()
            if cont == "y":
                print("Continue")
            else:
                print("Game over")
                break

        elif ((comp_choice == "R" and my_choice == "P") or
             (comp_choice == "P" and my_choice == "S") or
             (comp_choice == "R" and my_choice == "R")):
            print("You win")
            cont = input("Do you want to continue? (y/n): ").lower()
            if cont == "y":
                print("Continue")
            elif cont == "n":
                print("Game over")
                break
            else:
                print("Invalid choice!. Try again")

        else:
            print("Computer win")

            cont = input("Do you want to continue? (y/n): ").lower()
            if cont == "y":
                print("Continue")
            else:
                print("Game over")
                break







