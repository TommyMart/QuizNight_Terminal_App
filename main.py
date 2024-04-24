# System Packages
import os.path

# External Packages

# Import our own functions 
from quiz_functions import quiz_topics, random_quiz, top_scores, create_new

name = input("\nPlease enter your name: ")

print(f"\nHello {name}, and welcome to the Music Quiz!\n")

file_name = "list.csv"

# If the file doesn't exist we must create it with correct headings and then close it
if (not os.path.isfile(file_name)):
    print("creating file")
    high_scores = open(file_name, "w")
    high_scores.write("topic,score")
    high_scores.close()
    
def menu():
    
    print("1. Enter 1 for quiz topics")
    print("2. Enter 2 for top scores")
    print("3. Enter 3 to quick start a random quiz")
    print("4. Enter 4 to create a new text quiz")
    print("5. Enter 5 to exit quiz")

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
    

print("Thanks for playing the quiz, I hope you enjoyed yourself!")