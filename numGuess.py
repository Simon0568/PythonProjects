import random
import os
import sys
from time import sleep

# Pogadjanje broja, svaki put kad pocne partija dato je 5 poena, na svaku gresku se oduzima jedan i ako se stigne do 0, racunar je pobedio, ako ne, korisnik je pobedio i ispisuje se rezultat
#Ako je na kraju broj poena veci(ili jednak) od proslog High Score, prosli highscore = broj poena i ispisuje se datum i vreme u kojem ja napravljen novi highscore, highscore se moze prikazati pritiskom na taster 2 iz glavnog menija
high_score = 0
def menu():
    os.system('cls')
    print("Enter your choice:")
    print("1. Play\n2. High Scores\n3. Exit game\n")
    menu_choice = input()
    while(menu_choice not in ["1", "2", "3"]):
        print("Invalid choice, please choose between 1, 2 and 3...")
        menu_choice = input()
    if(menu_choice == "1"):
        game()
    elif(menu_choice == "2"):
        high_scores()
    else:
        exit()
    
    

def game():
    os.system('cls')
    global name
    name = input("What's your name? \n")
    print(f"Hello {name}, welcome to the game!\n")

    play_game = input("Do you want to play the game? Answer with a simple yes/no\n").lower()

    if(play_game == "no"):
        print("Okay, have a good one.")
        exit
    elif(play_game == "yes"):
        print("Starting the game...")
        game_start()
    else:
        print("That's not a valid option...")
        exit()
    
def game_start():
    global high_name
    global high_score
    global points
    os.system('cls')
    choice = 1
    points = 5
    again = "yes"

    random_num = random.randint(1, 10)
    print("This is a number guessing game, each time you play you'll be guessing a random number that i generated (1-10).\nAfter each miss, your points will be deducted, and if you reach zero... i win.")
    sleep(1) #CHANGE BACK TO 7
    while(points > 0 and again == "yes"):
        os.system('cls')
        print(random_num)
        guess = int(input("Input your guess: "))
        if(guess != random_num):
            print("Mistake.")
            points = points - 1
            print(f"Total points: {points}",)
            if(points == 0):
                print("You lose...")
                sleep(1)
                exit()
            else:
                sleep(1)
        else:
            print(f"Goodjob, you guessed the number! Total amount of points {points}")
            num = high_score
            if(points > num):
                num = points
                #new
                high_name = name
            again = input("Do you want to play again? yes/no...\n").lower()
            points = 5
            while(again not in ["yes", "no"]):
                again = input("Invalid choice, Do you want to play again? yes/no...\n").lower()
    print("Farewell...")
    high_score = num
    menu()

def high_scores():
    os.system('cls')
    try:
        print(f"Current highscore: \n\n{high_score} - {high_name}")
    except:
        print("There is no new high scores..")
    sleep(3)
    menu()

            

if __name__ == '__main__':
    menu()
    
