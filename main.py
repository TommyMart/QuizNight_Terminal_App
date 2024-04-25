# System Packages
import os.path
import csv
import random
import time

# External Packages
# from colorama import Fore, Style, Back
from rich import print 

# App functions
from quiz_functions import quiz_topics, random_quiz, top_scores, create_new

name = input("\nPlease enter your name: ").title()

# If no name is inputed name = Player
if name == "":
    name = "Player"

print(f"\nHello [bold black]{name}[/bold black], and welcome to [bold bright_cyan]Quiz Night[/bold bright_cyan]!\n")



def menu():
    print("[purple]-----------------------------[/purple]")
    print("    :vampire:    [bold blue]MAIN MENU[/bold blue]    :vampire: ")
    print("[purple]-----------------------------[/purple]\n")
    print("1. Enter 1 - to see [bold red]Quiz Topics[/bold red]")
    print("2. Enter 2 - to see your [bold yellow]Topic High Scores[/bold yellow]")
    print("3. Enter 3 - to quick start a [bold green]Random Quiz[/bold green]")
    print("4. Enter 4 - to try our [bold magenta]New Audio Based Quiz[/bold magenta]")
    print("5. Enter 5 - to [bold black]EXIT[/bold black] the game...")

    user_choice = input("\nPlease enter your selection: \n")
    return user_choice




choice = ""

while choice != "5":
    choice = menu()

    if choice == "1":
        quiz_topics()
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
    

print("Thanks for playing, we hope you enjoyed yourself!\n")