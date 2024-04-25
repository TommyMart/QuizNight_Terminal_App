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

print(f"\nHello {name}, and welcome to Quiz Night!\n")



def menu():
    print("-----------------------------")
    print("    :vampire:    MAIN MENU    :vampire: ")
    print("-----------------------------")
    print("1. Enter 1 to select a quiz topic")
    print("2. Enter 2 to see your topic high scores")
    print("3. Enter 3 to quick start a random quiz")
    print("4. Enter 4 to try our new audio based quiz")
    print("5. Enter 5 to exit the game")

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