#Skyler
import random
import time

def bank():
    global credits
    global balance
    balance=0
    while True:
        credit_loan=input("How much credit do you want to deposit? (20, 50, 100): ")
        try:
            if credit_loan=="20" or credit_loan=="50" or credit_loan=="100":
                credits+=int(credit_loan)
                print(f"Deposited {credit_loan}. Current balance: {credits}")
                break
            else:
                print("AMOUNT NOT ACCEPTED. PLEASE INSERT CORRECT AMOUNTS.")
        except:
            print("NOT A VIABLE DEPOSIT. TRY AGAIN.")

def spin():
    global credits
    credits-=10
    slot_1=random.choice(slot_list)
    slot_2=random.choice(slot_list)
    slot_3=random.choice(slot_list)
    print("Spinning Slots...")
    #time.sleep(3)
    print(f"Current Slots: [{slot_1}] [{slot_2}] [{slot_3}]")
    if slot_1=="7" and slot_2=="7" and slot_3=="7":
        print("JACKPOT!!! YOU WIN! +100 credits")
        credits+=100
    elif slot_1 == slot_2 == slot_3:
        print("You Win! +50 credits")
        credits+=50
    else:
        print("You lose! Better luck next time...")

#beginning
print("Welcome to the 3-slot Machine!")
credits=0
slot_list=["♈", "♊", "♋", "7"]
print(f"Slot Symbols: {slot_list}")
print(f"You have {credits} credits. Each spin costs 10 credits.")
bank()
print("")

while True:
    print(f"Credits: {credits}")
    lets_go_gambling=input("S to spin or Q to quit: ")
    if lets_go_gambling.upper().strip()=="S":
        if credits>=10:
            spin()
        else:
            print("INSUFFICIENT FUNDS. PLEASE INSERT CREDITS.")
            time.sleep(0.5)
            credits_bank=input("Deposit some credits? (Y/N): ")
            if credits_bank.title().strip()=="Y" or credits_bank.title().strip()=="Yes":
                print("Heading to bank...")
                time.sleep(1.5)
                bank()
    elif lets_go_gambling.upper().strip()=="B":
        print("Heading to bank...")
        time.sleep(0.5)
        bank()
    else:
        print("Thanks for playing!")
        print(f"Final Credits: {credits}!")
        break
#♈ ♊ ♋ 7
