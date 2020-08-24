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
    no = "400000"
    for i in range(10):
        no += str(random.randint(0, 9))
    return no
    
def generate_pin():
    no = ""
    for i in range(4):
        no += str(random.randint(0, 9))
    return no

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

