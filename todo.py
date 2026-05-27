#Skyler

#Init


todo_list = []

completed_list = []


decisions = 0
import time
while decisions != 4:
    print("Welcome to universal planner")
    #Functions
    time.sleep(0.7)
    print("---------------------------------------------------------")
    print("1. Add an item to the to-do list")
    time.sleep(0.3)
    print("2. Mark an item as Done")
    time.sleep(0.3)
    print("3. Remove an item or Clear the List")
    time.sleep(0.3)
    print("4. Exit the program")
    time.sleep(0.6)
    print(todo_list)
    time.sleep(0.3)
    print(completed_list)
    time.sleep(0.3)
    print("---------------------------------------------------------")
    decision = input("What would you like to do? (1,2,3,4): ")

    if decision == "1":
        add = input("What would you like to add on the to-do list?: ").strip()
        if add == "":
            print("---------------------------------------------------------")
            print("Error")
            print("---------------------------------------------------------")
        else:
            todo_list.append(add)
            time.sleep(0.7)
            print("---------------------------------------------------------")
            print("Item has been added!")
            time.sleep(0.5)
            print(todo_list)
            print("---------------------------------------------------------")
    elif decision == "2":
        print(todo_list)
        time.sleep(0.5)
        complete = input("What item have you completed?: ")
        if complete in todo_list:
            completed_list.append(complete)
            todo_list.remove(complete)
            time.sleep(0.5)
            print("---------------------------------------------------------")
            print("Item has been completed")
            print("---------------------------------------------------------")
        else:
            print("---------------------------------------------------------")
            print("Error")
            print("---------------------------------------------------------")
    elif decision == "3":
        print("---------------------------------------------------------")
        time.sleep(0.5)
        remove_clear = input("Would you like to remove or clear something? (r/c): ")
        if remove_clear == "r":
            print("---------------------------------------------------------")
            print(todo_list)
            removing = input("What do you want to remove?: ")
            if removing in todo_list:
                todo_list.remove(removing)
                time.sleep(0.7)
                print("Item has been removed from to-do list")
                print("---------------------------------------------------------")

        if remove_clear == "c":
            print("---------------------------------------------------------")
            print("Your items have been cleared")
            time.sleep(0.6)
            todo_list = []
            print("---------------------------------------------------------")
        else:
            print("---------------------------------------------------------")
            print("Error")
            print("---------------------------------------------------------")

    elif decision == "4":
        decisions = 4
        print("---------------------------------------------------------")
        print("Exiting . . .")
        print("---------------------------------------------------------")
    else:
        print("---------------------------------------------------------")
        time.sleep(0.5)
        print("Error")
        print("Retrying")
        print("---------------------------------------------------------")
