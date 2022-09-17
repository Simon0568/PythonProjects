import random
import os
from time import  sleep

choices = ["rock", "paper", "scissors"]

user_point = 0
computer_point = 0

while user_point != 3 and computer_point != 3:
    os.system('cls')

    user_choice = input("Enter your choice (rock, paper, scissors)\n").lower()

    while user_choice not in choices:
        user_choice = input("Enter your choice (rock, paper, scissors)\n").lower()


    computer_choice = random.choice(choices)



    # POSSIBLE COMBINATIONS
    # rock paper ==> paper wins
    # rock scissors ==> scissors win
    # scissors paper ==> scissors win
    # rock rock == > tie
    # scissors scissors ==> tie
    # scissors paper == > tie

    print(f"\n\nUser: {user_choice}\nComputer:{computer_choice}\n\n")


    if user_choice == computer_choice:
        print("Tie.\n")
    elif user_choice == "paper" and computer_choice == "rock" or user_choice == "rock" and computer_choice == "scissors" or user_choice == "scissors" and computer_choice == "paper":
        print("You win!\n")
        user_point += 1
    else:
        print("You lose!\n")
        computer_point += 1
    print(f"User score: {user_point}\nComputer score: {computer_point}")
    sleep(3)

os.system('cls')
print(f"FINAL SCORE\nUSER: {user_point}\nCOMPUTER: {computer_point}\n")
if computer_point == 3:
    print("Computer wins!")
else:
    print("User wins!")
sleep(2)