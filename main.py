# System Packages
import os.path
import csv
import random
import time

# External Packages
# from colorama import Fore, Style, Back
from rich import print 
from rich.console import Console
from rich.table import Table

# App functions
from quiz_functions import quiz_topics, random_quiz, top_scores, create_new

name = input("\nPlease enter your name: ").title()

# If no name is inputed name = Player
if name == "":
    name = "Player"

print(f"\nHello [bold black]{name}[/bold black], and welcome to [bold bright_cyan]Quiz Night[/bold bright_cyan]!\n")


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