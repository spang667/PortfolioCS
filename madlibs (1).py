#Skyler
#Madlibs
#A simulation of the popular madlibs game where silly stories sare generated using input from the player
#inlineSggest.enabled is sus
#Init
import time
import random

#Functions
random_words = ["crazy", "chaotic", "artistic", "suspicious"]
random_foods = ["pizza", "ice cream", "ramen", "rice"]
random_items = ["artifact", "mouse", "compass", "book"]

def madlibs():
    while True:
        print("Welcome to Madlibs!")

        #Gather input
        name = input("please type any name: ")
        time.sleep(.4)

        place = input("please type a place: ")
        time.sleep(.4)

        item = input("please type an item: ")
        time.sleep(.4)

        adjective = input("please type a describing word or (random word): ")
        if adjective.lower() == "random word":
            adjective = random.choice(random_words)
        time.sleep(.4)

        name1 = input("please type another name: ")
        time.sleep(.4)

        adjective1 = input("please type another describing word or (random word 2): ")
        if adjective1.lower() == "random word 2":
            adjective1 = random.choice(random_words)
        time.sleep(.4)

        food = input("please type a food or (random food): ")
        if food.lower() == "random food":
            food = random.choice(random_foods)
        time.sleep(.4)

        number = input("please type a postive number or (random number): ")
        if number.lower() == "random number":
            number = random.randint(1,100)
        time.sleep(.4)

        #Story
        print(f"\033[1m{name.upper()}\033[0m and I went to "f"\033[1m{place.upper()}\033[0m to get the infamous "f"\033[1m{item.upper()}\033[0m\n"
            f"which just so happened to be very "f"\033[1m{adjective.upper()}\033[0m. "f"You think that was the end of the story?\n"
            f"Well \033[1m{name1.upper()}\033[0m came along too and decided to\n"f"consume our interestingly "f"\033[1m{adjective1.upper()}\033[0m "f"\033[1m{food.upper()}\033[0m that we left in our pockets,\n"
            f"being over \033[1m{number}\033[0m days old.")

        replay = input("Play again(y/n)")
        if replay == "y":
            continue
        if replay == "n":
            data = [name, place, item, adjective, name1, adjective1, food, number]
            gamesession = [data]
            print("thanks for playing, you used")
            print(gamesession)
#main
madlibs()
