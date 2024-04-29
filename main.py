# System Packages
import os.path
import csv
import random
import time
import getpass

# External Packages
from rich import print 
from rich.console import Console
from rich.table import Table

# App functions
from quiz_functions import quiz_topics, random_quiz, top_scores, create_new



second_file_name = "user_names.csv"

    # If the file doesn't exist we must create it using the "w" or write
    # Add user_name and password and then close the file
    
if (not os.path.isfile(second_file_name)):
    user_names = open(second_file_name, "w")
    user_names.write("user_name,password\n")
    user_names.close()


def sign_up(second_file_name):
    while True:
        username = input("Enter a username: \n")
        # if len(username) < 5:   
        #     print("Username must be at least 5 characters long.\n")
        #     continue
        # password = getpass.getpass("Enter a password: \n")
        # if len(password) < 5:
        #     print("Password must be at least 5 characters long.\n")
        #     continue
        # with open(second_file_name, "a", newline="") as f:
        #     writer = csv.writer(f)
        #     writer.writerow([username, password])
        # print("Account created successfully!\n")
        return username

def sign_in(second_file_name):
    while True:
        username = input("Enter your username: \n")
        password = getpass.getpass("Enter your password: \n")
        with open(second_file_name, "r") as f:
            reader = csv.reader(f)
            next(reader)  
            found = False
            for row in reader:
                if row[0] == username and row[1] == password:
                    print(f"Welcome back {username}!\n")
                    found = True
                    return username
            if found:
                break
            else:
                print("Incorrect username or password. Please try again or sign up.\n")
                choice = input("Enter 'S' to sign up or any other key to try again: \n").upper()
                if choice == "S":
                    sign_up(second_file_name)
                    break

def topic_choice(choice):
    # choice = menu()

    if choice == "1":
        quiz_topics()
    elif choice == "2":
        top_scores()
    elif choice == "3":
        random_quiz()
    elif choice == "4":
        create_new()
    elif choice == "5":
        print("Thanks for playing Quiz Night, we hope you enjoyed yourself!\n")
    else: 
        print("Please only input options shown above.")


# menu = ""
def menu():
    console = Console()

    # Rich Main Menu table
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
    if user_choice == "5":
        return True
    else:
        topic_choice(user_choice)
        return False

def main():
    print("Welcome to Quiz Night!\n")
    while True:
        option = input("Are you a new user? (Y/N): \n").upper()
        if option == "Y":
            username = sign_up(second_file_name)
            break
        elif option == "N":
            username = sign_in(second_file_name)
            break
        else:
            print("Invalid input. Please enter Y or N.\n")
    while True:
        
        if menu():
            break
    
main()
# while True:
#     menu()
print("Thanks for playing Quiz Night, we hope you enjoyed yourself!\n")

    
# choice = ""



