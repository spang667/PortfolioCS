#Skyler
#simulate the rock paper scissors game against computer

#init
import random
import time
#functions

def rps():
    print("Welcome to rock, paper, scissors")
    W = 0
    L = 0
    while True:
        decision = input("rock, paper, or scissors?: ")
        time.sleep(1.5)
        x = random.randint(1,3)
        if x == 1:
            x = "rock"
        if x == 2:
            x = "paper"
        if x == 3:
            x = "scissors"
        if decision == "rock":
            print("You have chosen rock and you're going up against " + str(x))
            if x == "rock":
                print("The game resulted in a tie")
            elif x == "paper":
                print("You have lost the game")
                L = L + 1
            elif x == "scissors":
                print("You have won the game")
                W = W + 1
        if decision == "paper":
            print("You have chosen paper and you're going up against " + str(x))
            if x == "paper":
                print("The game resulted in a tie")
            elif x == "rock":
                print("You have won the game")
                W = W +1
            elif x == "scissors":
                print("You have lost the game")
                L= L + 1
        if decision == "scissors":
            print("You have chosen scissors and you're going up against " + str(x))
            if x == "scissors":
                print("The game resulted in a tie")
            elif x == "rock":
                print("You have lost the game")
                L = L + 1
            elif x == "paper":
                print("You have won the game")
                W= W +1
        if decision != "rock" and decision != "paper" and decision != "scissors":
            print("Invalid input, please try again")
            continue
        print("W: "+ str(W) + " L: " + str(L))
        play = input("Play again? (Y/N): ")
        if play.lower() == "y":
            continue
        if play.lower() == "n":
            break
#main
rps()
