# System Packages
import os.path
import csv
import random
import time
import getpass

# External Packages
# from colorama import Fore, Style, Back
from rich import print 
from rich.console import Console
from rich.table import Table

# App functions
from quiz_functions import quiz_topics, random_quiz, top_scores, create_new



second_file_name = "user_names.csv"

    # If the file doesn't exist we must create it
    # Add user_name and password and then close the file
if (not os.path.isfile(second_file_name)):
    user_names = open(second_file_name, "w")
    user_names.write("user_name,password\n")
    user_names.close()


def sign_up(second_file_name):
    while True:
        username = input("Enter a username: \n")
        if len(username) < 5:
            print("Username must be at least 5 characters long.\n")
            continue
        password = getpass.getpass("Enter a password: \n")
        if len(password) < 5:
            print("Password must be at least 5 characters long.\n")
            continue
        with open(second_file_name, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([username, password])
        print("Account created successfully!\n")
        break

def sign_in(second_file_name):
    while True:
        username = input("Enter your username: \n")
        password = getpass.getpass("Enter your password: \n")
        with open(second_file_name, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            found = False
            for row in reader:
                if row[0] == username and row[1] == password:
                    print("Welcome back!")
                    found = True
                    break
            if found:
                break
            else:
                print("Incorrect username or password. Please try again or sign up.\n")
                choice = input("Enter 'S' to sign up or any other key to try again: \n").upper()
                if choice == "S":
                    sign_up(second_file_name)
                    break

def main():
    
    
    print("Welcome to Quiz Night!\n")
    while True:
        option = input("Are you a new user? (Y/N): \n").upper()
        if option == "Y":
            sign_up(second_file_name)
            break
        elif option == "N":
            sign_in(second_file_name)
            break
        else:
            print("Invalid input. Please enter Y or N.\n")

main()
# sign_in = ""

# def signin(sign_in):
#     sign_in = input("\nHello, is this your first time playing Quiz Night Y/N? \n").upper()

#     if sign_in == "Y":
#         print("Welcome to Quiz Night!\n")
#         while True:
#             user_name = input("Please enter a username: \n").title()
#             if len(user_name) < 5:
#                 print(f"Username must be more than 5 characters long.\n")
#             else:
#                 break   
#         while True:
#             password = getpass.getpass("Please enter a password: \n")
#             if len(password) < 5:
#                 print(f"Password must be longer than 5 characters long.\n")
#             else:
#                 break
                
#         with open(second_file_name, "a") as f:
#             writer = csv.writer(f)
#             writer.writerow([user_name, password])
#         print(f"Welcome {user_name} to Quiz Night!\n")
#     elif sign_in == "N":
#         while True:
#             user_name = input("Please enter your username: \n").title()
#             with open(second_file_name, "r") as f:
#                 reader = csv.reader(f)
#                 found = False
#                 for i in reader:
#                     if i[0] == user_name:
#                         found = True
#                         break
#                     else:
#                         break
#             password = getpass.getpass("Please enter your password: \n")
#             if len(password) < 5:
#                 print(f"Password must be longer than 5 characters long.\n")
#             else:
#                 break
#             with open(second_file_name, "r") as f:
#                 reader = csv.reader(f)
#                 found = False
#                 for i in reader:
#                     if i[0] == user_name and i[1] == password:
#                         found = True
#                         print("Welcome to Quiz Night!\n")
#                         break
#                 if found: 
#                     break
#                 else:
#                     print("Incorrect username or password. Please try again\n")
#                     back = input("Or enter B to enter a new username. \n").upper
#                     if back == "B":
#                         break  
                  
#     else:
#         print("Invalid input. Please enter Y or N.\n")  

# signin(sign_in)

# user_name = input("Please enter your username: ")
#     if user_name is in user_names
#     password = input()
# with open(user_names, "a") as f:
#         writer = csv.writer(f)
#         writer.writerow([user_name, password])

# user_name = input("\nPlease enter your name: ").title()

# If no name is inputed name = Player


#print(f"\nHello [bold black]{user_name}[/bold black], and welcome to [bold bright_cyan]Quiz Night[/bold bright_cyan]!\n")


def menu():
    console = Console()

    # Create a rich table
    table = Table(title=":vampire:  MAIN MENU  :vampire:", style="bold purple", show_lines=True, title_style="bold black on purple")
    table.add_column("Selection", style="bold cyan", justify="left")
    table.add_column("Option", style="bold cyan", justify="left")

    table.add_row("1", "Quiz Topics")
    table.add_row("2", "Topic High Scores")
    table.add_row("3", "Quick Start Random Quiz")
    table.add_row("4", "New Audio Based Quiz")
    table.add_row("5", "[bright_red]EXIT[/bright_red]")


    console.print(table)

    user_choice = input("Please enter your selection: \n")
    return user_choice



choice = ""

while choice != "5":
    choice = menu()

    if choice == "1":
        quiz_topics(username)
    elif choice == "2":
        top_scores()
    elif choice == "3":
        random_quiz()
    elif choice == "4":
        create_new()
    elif choice == "5":
        print("5")
    else: 
        print("Please only input options shown above.")
    

print("Thanks for playing Quiz Night, we hope you enjoyed yourself!\n")