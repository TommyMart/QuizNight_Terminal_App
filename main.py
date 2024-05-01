# System Packages
import os.path
import csv
import getpass

# External Packages
from rich import print 
from rich.console import Console
from rich.table import Table

# App functions
from quiz_functions import quiz_topics, random_quiz, top_scores, instructions

# Create a variable and assign it to the csv file
second_file_name = "user_names.csv"

    # If the file doesn't exist we must create it using the "w" (write mode)
    # Add user_name and password and then close the file
if (not os.path.isfile(second_file_name)):
    user_names = open(second_file_name, "w")
    user_names.write("user_name,password\n")
    user_names.close()

# Sign up function
def sign_up(second_file_name):
    while True:
        username = input("Please enter a username: \n")
        if len(username) < 5:   
            print("Username must be at least 5 characters long.\n")
            continue
        password = getpass.getpass("Please enter a password: \n")
        if len(password) < 5:
            print("Password must be at least 5 characters long.\n")
            continue
        with open(second_file_name, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([username, password])
        print("Account created successfully.\n")
        print(f"Welcome to Quiz Night {username}!\n")
        return username
    
# Sign in function
def sign_in(second_file_name):
    while True:
        username = input("Please enter your username: \n")
        password = getpass.getpass("Please enter your password: \n")
        with open(second_file_name, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip headings
            found = False
            for row in reader:
                if row[0] == username and row[1] == password:
                    print(f"Welcome back to Quiz Night {username}!\n")
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

# Main menu selection function call
def topic_choice(choice, username):
    if choice == "1":
        quiz_topics(username)
    elif choice == "2":
        top_scores()
    elif choice == "3":
        random_quiz(username)
    elif choice == "4":
        instructions()
    elif choice == "5":
        return
    else: 
        print("Please only input options shown above.")

# Main Menu Table & Input
def menu(username):
    console = Console()

    # Rich Main Menu table data
    table = Table(title=":vampire:  MAIN MENU  :vampire:", style="bold purple", show_lines=True, title_style="bold black on purple")
    table.add_column("Selection", style="bold cyan", justify="left")
    table.add_column("Option", style="bold cyan", justify="left")

    # Table selections
    table.add_row("1", "Quiz Topics")
    table.add_row("2", "Topic High Scores")
    table.add_row("3", "Quick Start Random Quiz")
    table.add_row("4", "Quiz Instructions")
    table.add_row("5", "[bright_red]EXIT[/bright_red]")

    # Print table
    console.print(table)

    # User menu selection
    user_choice = input("Please enter your selection: \n")
    if user_choice == "5":
        return True
    else:
        topic_choice(user_choice, username)
        return False

# First main function directing users to sign in or up
def main():
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
        if menu(username):
            break

# Call main function to start the user experience   
main()

# User has selected 5 from the main menu and wishes to exit the app
print("\nGoodbye, we hope to see you again soon!\n")
    




