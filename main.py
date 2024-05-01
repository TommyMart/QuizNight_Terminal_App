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


# Sign up function
def sign_up():

    # Create a variable and assign it to the csv file that will be created
    # next
    second_file_name = "user_names.csv"

    try:
        # If the csv file doesn't exist we must create it using the "w" (write mode)
        if (not os.path.isfile(second_file_name)):
            user_names = open(second_file_name, "w")
            # Add user_name and password headings and then close the file
            user_names.write("user_name,password\n")
            user_names.close()

    except: 
        # Unexpected Error Handling
        print("Oops! Something seems to be not working, please try again.")

    try:
        while True:
            # Input new username that's 5 characters or longer
            username = input("Please enter a username: \n")

            if len(username) < 5:   
                print("Username must be at least 5 characters long.\n")
                continue       
            # Input new password that's 5 characters or longer
            password = getpass.getpass("Please enter a password: \n")

            if len(password) < 5:
                print("Password must be at least 5 characters long.\n")
                continue            

            # Open csv file in append mode and write the new username and 
            # password to a new row
            with open(second_file_name, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([username, password])

            print("Account created successfully.\n")
            print(f"Welcome to Quiz Night {username}!\n")

            # Return username so it can be used in other functions
            return username
        
    except: 
        # Unexpected Error Handling
        print("Oops! Something seems to be not working, please try again.")


# Sign in function
def sign_in():
    try:
        while True:
            # Ask user to enter previous username
            username = input("Please enter your username: \n")
            # Ask user to enter previous password
            password = getpass.getpass("Please enter your password: \n")

            # Open csv username and password file in read mode
            with open(second_file_name, "r") as f:
                reader = csv.reader(f)
                # Skip headings
                next(reader)  
                found = False

                # Loop through each row in csv file to see if the username and password 
                # matches an existing username
                for row in reader:

                    if row[0] == username and row[1] == password:
                        # Welcome user back to app
                        print(f"Welcome back to Quiz Night {username}!\n")
                        found = True
                        # Return username so it can be used in other functions
                        return username
                    
                if found:
                    break

                # If cannot find a username and password match, display incorrect username
                # or password to user and give them an option to sign up instead 'S'
                else:
                    print("Incorrect username or password. Please try again or sign up.\n")
                    choice = input("Enter 'S' to sign up or any other key to try again: \n").upper()
                    if choice == "S":
                        sign_up(second_file_name)
                        break

    except: 
        # Unexpected Error Handling
        print("Oops! Something seems to be not working, please try again.")


# Main menu selection function call
def topic_choice(choice, username):

    # If user selects 1 call quiz_topics function
    if choice == "1":
        quiz_topics(username)

    # If user slects 2 call top_scores function
    elif choice == "2":
        top_scores()

    # If user selects 3 call random_quiz function
    elif choice == "3":
        random_quiz(username)

    # If user selects 4 call instructions function
    elif choice == "4":
        instructions()

    # Error handling if the user input is invalid
        print("Please only input options shown above.")


# Main Menu Table & Input
def menu(username):

    try:
        console = Console()

        # Rich Main Menu table data - Heading, Selection and Option column options
        table = Table(title=":vampire:  MAIN MENU  :vampire:", style="bold purple", 
                    show_lines=True, title_style="bold black on purple")
        table.add_column("Selection", style="bold cyan", justify="left")
        table.add_column("Option", style="bold cyan", justify="left")

        # Main Menu selections
        table.add_row("1", "Quiz Topics")
        table.add_row("2", "Topic High Scores")
        table.add_row("3", "Quick Start Random Quiz")
        table.add_row("4", "Quiz Instructions")
        table.add_row("5", "[bright_red]EXIT[/bright_red]")

        # Print table
        console.print(table)

        # User menu selection
        user_choice = input("Please enter your selection: \n")

        # If user enters five exit the app
        if user_choice == "5":
            return True
        # Calls topic_choice function with the user's choice
        else:
            topic_choice(user_choice, username)
            return False
        
    except: 
        # Unexpected Error Handling
        print("Oops! Something seems to be not working, please try again.")


# First main function directing users to sign in or up
def main():
    try: 
        # Ask user if they're a new or returning
        while True:
            option = input("Are you a new user? (Y/N): \n").upper()
            # If yes call sign_up function
            if option == "Y":
                username = sign_up()
                break
            # If no - call sign in function 
            elif option == "N":
                username = sign_in()
                break
            # Error handling if the user enters anything other than Y or N
            else:
                print("Invalid input. Please enter Y or N.\n")

        while True:

            if menu(username):
                break

    except: 
        # Unexpected Error Handling
        print("Oops! Something seems to be not working, please try again.")


# Call main function to start the user experience   
main()


# User has selected 5 from the main menu and wishes to exit the app
print("\nGoodbye, we hope to see you again soon!\n")
    




