import os
import random


def decisionMaker():
    os.system('cls')
    decisions = []
    
    try:
        n = int(input("How many decisions do you have?\n"))
    except:
        print("Not a number")
        exit()

    for i in range(n):
        decision = input(f"Decision no {i+1}: ")
        decisions.append(decision)

    print(f"You should try: {random.choice(decisions)}")

decisionMaker()