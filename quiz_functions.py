# System Packages
import os.path
import csv
import random

# External Packages
from colorama import Fore, Style, Back

# App functions
from quizzes import quiz

def quiz_topics(rand_quiz=None):
    print("\nQUIZ TOPICS\n")
    print("1. Enter 1 for Pop Culture")
    print("2. Enter 2 for 70's")
    print("3. Enter 3 for 80's")
    print("4. Enter 4 for 90's Hip Hop")
    print("5. Enter 5 for Rock n Roll")
    print("6. Back to main menu")


    if rand_quiz is None:
        topic_choice = input("\nPlease enter your selection: \n")
    else: 
        topic_choice = str(rand_quiz)

# Pop Quiz selected

    if topic_choice == "1": 
        
        questions = (("\nWhat name is NOT one of Kim or Kanye's children?: \n"), 
                 ("\nWhich pop star is the godmother of both of Elton John's sons?: \n"), 
                 ("\nWhat is Rihanna's real name?: \n"), 
                 ("\nWhich pop star accidentally set fire to her home gym with candles?: \n"),
                 ("\nWhich pop star was Judge Judy's neighbor?: \n"),
                 )

        options = ((Fore.CYAN + Back.LIGHTGREEN_EX + "A. Chicago", "B. East", "C. Palm", "D. North"),
               ("A. Mariah Carey", "B. Tina Turner", "C. Lady Gaga", "D. Madonna"),
               ("A. Rihanna Felty", "B. Robyn Fenty", "C. Robin Dern", "D. Rachel Feaner"),
               ("A. Lady Gaga", "B. Rihanna", "C. Miley Cyrus", "D. Britney Spears"),
               ("A. Justin Bieber", "B. Adele", "C. Taylor Swift", "D. Bruno Mars"),
    )

        answers = ("B", "C", "B", "D", "A")
        quiz(questions, options, answers, topic_choice)
        
# 70's Quiz Selected

    elif topic_choice == "2":
        questions = (("\nWhat name is NOT one of Kim or Kanye's children?: \n"), 
                 ("\nWhich pop star is the godmother of both of Elton John's sons?: \n"), 
                 ("\nWhat is Rihanna's real name?: \n"), 
                 ("\nWhich pop star accidentally set fire to her home gym with candles?: \n"),
                 ("\nWhich pop star was Judge Judy's neighbor?: \n"),
                 )

        options = ((Fore.CYAN + Back.LIGHTGREEN_EX + "A. Chicago", "B. East", "C. Palm", "D. North"),
               ("A. Mariah Carey", "B. Tina Turner", "C. Lady Gaga", "D. Madonna"),
               ("A. Rihanna Felty", "B. Robyn Fenty", "C. Robin Dern", "D. Rachel Feaner"),
               ("A. Lady Gaga", "B. Rihanna", "C. Miley Cyrus", "D. Britney Spears"),
               ("A. Justin Bieber", "B. Adele", "C. Taylor Swift", "D. Bruno Mars"),
    )

        answers = ("B", "C", "B", "D", "A")
        quiz(questions, options, answers, topic_choice)

# 80s Quiz Selected 

    elif topic_choice == "3":
        questions = (("\nWhat name is NOT one of Kim or Kanye's children?: \n"), 
                 ("\nWhich pop star is the godmother of both of Elton John's sons?: \n"), 
                 ("\nWhat is Rihanna's real name?: \n"), 
                 ("\nWhich pop star accidentally set fire to her home gym with candles?: \n"),
                 ("\nWhich pop star was Judge Judy's neighbor?: \n"),
                 )

        options = ((Fore.CYAN + Back.LIGHTGREEN_EX + "A. Chicago", "B. East", "C. Palm", "D. North"),
               ("A. Mariah Carey", "B. Tina Turner", "C. Lady Gaga", "D. Madonna"),
               ("A. Rihanna Felty", "B. Robyn Fenty", "C. Robin Dern", "D. Rachel Feaner"),
               ("A. Lady Gaga", "B. Rihanna", "C. Miley Cyrus", "D. Britney Spears"),
               ("A. Justin Bieber", "B. Adele", "C. Taylor Swift", "D. Bruno Mars"),
    )

        answers = ("B", "C", "B", "D", "A")
        quiz(questions, options, answers, topic_choice)

    elif topic_choice == "4":
        questions = (("\nWhat name is NOT one of Kim or Kanye's children?: \n"), 
                 ("\nWhich pop star is the godmother of both of Elton John's sons?: \n"), 
                 ("\nWhat is Rihanna's real name?: \n"), 
                 ("\nWhich pop star accidentally set fire to her home gym with candles?: \n"),
                 ("\nWhich pop star was Judge Judy's neighbor?: \n"),
                 )

        options = ((Fore.CYAN + Back.LIGHTGREEN_EX + "A. Chicago", "B. East", "C. Palm", "D. North"),
               ("A. Mariah Carey", "B. Tina Turner", "C. Lady Gaga", "D. Madonna"),
               ("A. Rihanna Felty", "B. Robyn Fenty", "C. Robin Dern", "D. Rachel Feaner"),
               ("A. Lady Gaga", "B. Rihanna", "C. Miley Cyrus", "D. Britney Spears"),
               ("A. Justin Bieber", "B. Adele", "C. Taylor Swift", "D. Bruno Mars"),
    )

        answers = ("B", "C", "B", "D", "A")
        quiz(questions, options, answers, topic_choice)

    elif topic_choice == "5":
        questions = (("\nWhat name is NOT one of Kim or Kanye's children?: \n"), 
                 ("\nWhich pop star is the godmother of both of Elton John's sons?: \n"), 
                 ("\nWhat is Rihanna's real name?: \n"), 
                 ("\nWhich pop star accidentally set fire to her home gym with candles?: \n"),
                 ("\nWhich pop star was Judge Judy's neighbor?: \n"),
                 )

        options = ((Fore.CYAN + Back.LIGHTGREEN_EX + "A. Chicago", "B. East", "C. Palm", "D. North"),
               ("A. Mariah Carey", "B. Tina Turner", "C. Lady Gaga", "D. Madonna"),
               ("A. Rihanna Felty", "B. Robyn Fenty", "C. Robin Dern", "D. Rachel Feaner"),
               ("A. Lady Gaga", "B. Rihanna", "C. Miley Cyrus", "D. Britney Spears"),
               ("A. Justin Bieber", "B. Adele", "C. Taylor Swift", "D. Bruno Mars"),
    )

        answers = ("B", "C", "B", "D", "A")
        quiz(questions, options, answers, topic_choice)

    elif topic_choice == "6":
        return 
    else: 
        print("Please only input corresponding topic numbers shown above.")
        quiz_topics()
            
def top_scores():
    print(Fore.MAGENTA + "-----------------------------")
    print("      QUIZ HIGH SCORES!     ")
    print("-----------------------------" + Style.RESET_ALL)
    file_name = "list.csv"

    with open(file_name, "r") as f:
        reader = csv.reader(f)
        # reader.__next__()

        pop_highscores = []
        seventies_highscores = []
        eighties_highscores = []
        hiphop_highscores = []
        rocknroll_highscores = []

        for i in reader:
            if i[0] == "1":
                pop_highscores.append(float(i[1]))
            elif i[0] == "2":
                seventies_highscores.append(float(i[1]))
            elif i[0] == "3":
                eighties_highscores.append(float(i[1]))
            elif i[0] == "4":
                hiphop_highscores.append(float(i[1]))
            elif i[0] == "5":
                rocknroll_highscores.append(float(i[1]))

        pop_highscores.sort(reverse=True)

        seventies_highscores.sort(reverse=True)   
        eighties_highscores.sort(reverse=True)
        hiphop_highscores.sort(reverse=True)
        rocknroll_highscores.sort(reverse=True)

        
        
        if not pop_highscores:
            print("You have not attempted the Pop quiz yet.")
        else:
            print(f"Your highest Pop quiz score is {pop_highscores[0]:.4f}!")
        if not seventies_highscores:
            print("You have not attempted the 70's quiz yet.")
        else:
            print(f"Your highest 70's quiz score is {seventies_highscores[0]:.4f}!")
        if not eighties_highscores:
            print("You have not attempted the 80's quiz yet.")
        else:
            print(f"Your highest 80's quiz score is {eighties_highscores[0]:.4f}!")
        if not hiphop_highscores:
            print("You have not attempted for the 90's Hip Hop quiz yet.")
        else: 
            print(f"Your highest 90's Hip Hop quiz score is {hiphop_highscores[0]:.4f}!")
        if not rocknroll_highscores:
            print("You have not attempted the Rock N Roll quiz yet.")
        else:
            print(f"Your highest Rock N Roll quiz score is {rocknroll_highscores[0]:.4f}!\n")

        input("Press any key for main menu: \n")

def random_quiz():
    rand_quiz = random.randint(1, 5)
    quiz_topics(rand_quiz)
    

def create_new():
    print("new")

