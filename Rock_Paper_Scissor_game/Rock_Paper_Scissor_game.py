"""
Docstring for Rock_Paper_Scissor_Game

1. User Input
2. Python Random Function use
3. Print

Case :
 1. Rock
 Rock - Rock = Tie
 Rock - Paper = Paper win
 Rock - Scissor = Rock Win

 2. Paper
 Paper - Paper = tie
 Paper - Rock = Paper Win
 Paper - Scissor = Scissor win

 2. Scissor
 Scissor - Scissor = tie
 Scissor - Rock = Rock win
 Scissor - Paper = Scissor win


"""

import random

item_list = ['Rock', 'Paper','Scissor']

user_choice = input("Enter Your Move =  Rock , Paper, Scissor : ")
com_choice = random.choice(item_list)

print(f" User Choice = {user_choice}, Computer Choice = {com_choice}")

if user_choice == com_choice:
    print("Both Chooses Same Result = Tie")

elif user_choice == "Rock":
    if com_choice == "Paper":
        print(" Paper Cover Rocks Resut = Computer Win")
    else:
        print("Rock Smashes Scissor Resutl = You Win")


elif user_choice == "Paper":
    if com_choice == "Rock":
        print(" Paper Cover Rocks  Result = You Win")
    else:
        print("Scissor Cuts Paper Resutl = Computer Win")

elif user_choice == "Scissor":
    if com_choice == "Rock":
        print("Rock Smashes Scissor Resutl = Computer Win")
    else:
       print ("Scissor Cuts Paper Resutl = You Win")