#Skyler
#Create a program that prompts the user for their name and simulates being assigned one of the 4 hogwarts houses
import random
import time


def house(name):
    x = random.randint(1,4)
    if name == "harry" or name == "ron" or name == "hermione":
        return "Your house is Gryffindor"
    elif name == "newt" or name == "nymphadora" or name == "ponoma":
        return "Your house is Hufflepuff"
    if name == "luna" or name == "cho" or name == "filius":
        return "Your house is Ravenclaw"
    elif name == "voldemort" or name == "draco" or name == "severus":
        return "Your house is Slytherin"
    if x == 1:
        return "Your house is Gryffindor"
    elif x == 2:
        return "Your house is Hufflepuff"
    elif x == 3:
        return "Your house is Ravenclaw"
    elif x == 4:
        return "Your house is Slytherin"
    if house(name) == "Your house is Gryffindor":
        x = random.randint(2,4)
    if house(name) == "Your house is Hufflepuff":
        x = random.randint(1,3,4)
    if house(name) == "Your house is Ravenclaw":
        x = random.randint(1,2,4)
    if house(name) == "Your house is Slytherin":
        x = random.randint(1,3)
def main():
    print("Welcome to Hogwarts")
    name = str.lower(input("What is your name?: "))
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print(house(name))
main()
while True:
    redo = input("Would you like to get reassigned into another house? (yes/no): ").lower()
    if redo == "yes":
        main()
    if redo == "no":
        print("Welcome to your house")
        break
    if redo != "yes" and redo != "no":
        print("You wrote something wrong")


