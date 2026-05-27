#Skyler AND Boris
import time
import random

def countdown(seconds):
    while seconds > 0:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)  # Pause for 1 second
        seconds -= 1

def game():
    print("Welcome to the guessing game!")
    difficulty=input("What difficulty would you like to play at? (easy, medium, hard): ")
    if difficulty == "easy":
        easy_game()
    if difficulty == "medium":
        medium_game()
    if difficulty == "hard":
        hard_game()

def easy_game():
    x = random.randint(1,5)
    max_tries = 5
    while True:
        number = input("pick a number between 1 - 5: ")
        countdown(5)
        if x > int(number):
            print("too low")
            max_tries=max_tries-1
            print(f"You have {max_tries} attempts left")
            if max_tries == 0:
                print("You reached the max amount of tries")
                break
            continue
        if x < int(number):
            print("too high")
            max_tries=max_tries-1
            print(f"You have {max_tries} attempts left")
            if max_tries == 0:
                print("You reached the max amount of tries")
                break
            continue
        if int(number) == x:
            print("YOU GUESSED THE NUMBER")
            break
def medium_game():
    x = random.randint(1,10)
    max_tries = 4
    while True:
        number = input("pick a number between 1 - 10: ")
        start_time=time.time()
        if x > int(number):
            print("too low")
            max_tries=max_tries-1
            print(f"You have {max_tries} attempts left")
            if max_tries == 0:
                print("You reached the max amount of tries")
                break
            continue
        if x < int(number):
            print("too high")
            max_tries=max_tries-1
            print(f"You have {max_tries} attempts left")
            if max_tries == 0:
                print("You reached the max amount of tries")
                break
            continue
        if int(number) == x:
            print("YOU GUESSED THE NUMBER")
            break

def hard_game():
    x=random.randint(1,20)
    max_tries=3
    while True:
        number = input("pick a number between 1 - 20: ")
        countdown(10)
        if x > int(number):
            print("too low")
            max_tries=max_tries-1
            print(f"You have {max_tries} attempts left")
            if max_tries == 0:
                print("You reached the max amount of tries")
                break
            continue
        if x < int(number):
            print("too high")
            max_tries=max_tries-1
            print(f"You have {max_tries} attempts left")
            if max_tries == 0:
                print("You reached the max amount of tries")
                break
            continue
        if int(number) == x:
            print("YOU GUESSED THE NUMBER")
            break
game()
