import random
import os
from time import sleep

# Pogadjanje broja, svaki put kad pocne partija dato je 5 poena, na svaki promaseni pokusaj se oduzima jedan i ako se stigne do 0, racunar je pobedio, ako ne, korisnik je pobedio i ispisuje se rezultat

def menu():
    os.system('cls')
    global name
    name = input("What's your name? \n")
    print(f"Hello {name}, welcome to the game!\n")

    play_game = input("Do you want to play the game? Answer with a simple yes/no\n")

    if(play_game.lower() == "no"):
        print("Okay, have a good one.")
        exit
    elif(play_game.lower() == "yes"):
        print("Starting the game...")
        game_start()
    else:
        print("That's not a valid option...")
    

def game_start():
    os.system('cls')
    choice = 1
    #while loop should start here

    random_num = random.randint(1, 10)
    print("This is a number guessing game, each time you play you'll be guessing a random number that i generated.\nAfter each miss, your points will be deducted, and if you reach zero... i win.")
    sleep(7)
    os.system('cls')
    guess = input("Input your guess: ")
    if(guess != random_num):
        print("Mistake.")
        exit
    else:
        print("First try.")

"""
while(choice == 1):


    choice = input("Do you want to keep playing? 1=yes 2=no")


"""
    





if __name__ == '__main__':
    menu()
    
