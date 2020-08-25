import random
import sys

cc_numbers = []
account_info = {}

def start():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    global cc_numbers 
    global account_info
    choice = start_choice()
    if choice == "1":
        cc_no = generate_cc()
        pin = generate_pin()
        
        cc_numbers.append(cc_no)
        account_info[cc_no] = pin
        
        print("\nYour card has been created\nYour card number:")
        print(f"{cc_no}\nYour card PIN:\n{pin}\n")
        start()
    
    elif choice == "2":
        print("\nEnter your card number:")
        entered_no = input(">")
        print("Enter your PIN:")
        entered_pin = input(">")
        if entered_no not in cc_numbers or account_info[entered_no] != entered_pin:
            print("\nWrong card number or PIN!\n")
            start()
        else:
            log_in_page()
            

    elif choice == "0":
        exit()   
    
def generate_cc():
    bank_id_no = "400000"
    for i in range(9): # Account Identifier.
        bank_id_no += str(random.randint(0, 9))

    cont = []
    for num in bank_id_no[0::2]: # multiply odd digits by 2, Luhn's algorithm.
        cont.append(int(num) * 2)

    for num in bank_id_no[1::2]: # gather all even digits.
        cont.append(int(num))

    newcont = []
    for num in cont: # subtract 9 from any digit greater than 9.
        if num > 9:
            newcont.append(num - 9)
        else:
            newcont.append(num)

    final = sum(newcont)
    for i in range(0, 10): # Find the number that when added to the sum of the previous 15 numbers, is divisible by 10.
        if (i + final) % 10 == 0:
            bank_id_no += str(i) # This will be the "checksum".
    
    return bank_id_no
    
def generate_pin():
    pin = ""
    for i in range(4):
        pin += str(random.randint(0, 9))
    return pin

def exit():
    sys.exit("Bye!")

def log_in_page():
    print("\nYou have successfully logged in!\n\n1. Balance\n2. Log out\n0. Exit")
    log_in_choice = input(">")
    if log_in_choice == "1":
        print("\nBalance: 0\n")
        log_in_page()
    elif log_in_choice == "2":
        print("\nYou have successfully logged out!\n\n")
        start()
    elif log_in_choice == "0":
        exit()

def start_choice():
    choice = input(">")
    return choice

start()

