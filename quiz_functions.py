# System Packages
import os.path
import csv
import random

# External Packages
# from colorama import Fore, Style, Back
from rich import print 

# App functions
from quizzes import quiz

def quiz_topics(rand_quiz=None):
    print("[purple]-----------------------------[/purple]")
    print("    :microbe:  [bold red]QUIZ TOPICS  [bold red] :microbe:")
    print("[purple]-----------------------------[/purple]\n")
    print("1. Enter 1 - for [bold blue]Music[/bold blue] :microphone:")
    print("2. Enter 2 - for [bold green]History[/bold green] :book:")
    print("3. Enter 3 - for [bold magenta]Capital Cities[/bold magenta] :house:")
    print("4. Enter 4 - for [bold yellow]Computer Science[/bold yellow] :dvd:")
    print("5. Enter 5 - for [bold red]General Knowledge[/bold red] :microbe:")
    print("6. Enter 6 - to return to [bold black]main menu[/bold black]")


    if rand_quiz is None:
        topic_choice = input("\nPlease enter your selection: \n")
    else: 
        topic_choice = str(rand_quiz)

# Music Quiz

    if topic_choice == "1": 
        
        questions = (("\nWhat name is NOT one of Kim or Kanye's children?: \n"), 
                 ("\nWhich pop star is the godmother of both of Elton John's sons?: \n"), 
                 ("\nWhat is Rihanna's real name?: \n"), 
                 ("\nWhich pop star accidentally set fire to her home gym with candles?: \n"),
                 ("\nWhich pop star was Judge Judy's neighbor?: \n"),
                 )

        options = (("A. Chicago", "B. East", "C. Palm", "D. North"),
               ("A. Mariah Carey", "B. Tina Turner", "C. Lady Gaga", "D. Madonna"),
               ("A. Rihanna Felty", "B. Robyn Fenty", "C. Robin Dern", "D. Rachel Feaner"),
               ("A. Lady Gaga", "B. Rihanna", "C. Miley Cyrus", "D. Britney Spears"),
               ("A. Justin Bieber", "B. Adele", "C. Taylor Swift", "D. Bruno Mars"),
    )

        answers = ("B", "C", "B", "D", "A")
        quiz(questions, options, answers, topic_choice)
        
# History Quiz 

    elif topic_choice == "2":
        questions = (("\nWhat name is NOT one of Kim or Kanye's children?: \n"), 
                 ("\nWhich pop star is the godmother of both of Elton John's sons?: \n"), 
                 ("\nWhat is Rihanna's real name?: \n"), 
                 ("\nWhich pop star accidentally set fire to her home gym with candles?: \n"),
                 ("\nWhich pop star was Judge Judy's neighbor?: \n"),
                 )

        options = (("A. Chicago", "B. East", "C. Palm", "D. North"),
               ("A. Mariah Carey", "B. Tina Turner", "C. Lady Gaga", "D. Madonna"),
               ("A. Rihanna Felty", "B. Robyn Fenty", "C. Robin Dern", "D. Rachel Feaner"),
               ("A. Lady Gaga", "B. Rihanna", "C. Miley Cyrus", "D. Britney Spears"),
               ("A. Justin Bieber", "B. Adele", "C. Taylor Swift", "D. Bruno Mars"),
    )

        answers = ("B", "C", "B", "D", "A")
        quiz(questions, options, answers, topic_choice)

# Capital Cities Quiz 

    elif topic_choice == "3":
        questions = (("\nWhat name is NOT one of Kim or Kanye's children?: \n"), 
                 ("\nWhich pop star is the godmother of both of Elton John's sons?: \n"), 
                 ("\nWhat is Rihanna's real name?: \n"), 
                 ("\nWhich pop star accidentally set fire to her home gym with candles?: \n"),
                 ("\nWhich pop star was Judge Judy's neighbor?: \n"),
                 )

        options = (("A. Chicago", "B. East", "C. Palm", "D. North"),
               ("A. Mariah Carey", "B. Tina Turner", "C. Lady Gaga", "D. Madonna"),
               ("A. Rihanna Felty", "B. Robyn Fenty", "C. Robin Dern", "D. Rachel Feaner"),
               ("A. Lady Gaga", "B. Rihanna", "C. Miley Cyrus", "D. Britney Spears"),
               ("A. Justin Bieber", "B. Adele", "C. Taylor Swift", "D. Bruno Mars"),
    )

        answers = ("B", "C", "B", "D", "A")
        quiz(questions, options, answers, topic_choice)

# Computer Science Quiz 

    elif topic_choice == "4":
        questions = (("\nWhat name is NOT one of Kim or Kanye's children?: \n"), 
                 ("\nWhich pop star is the godmother of both of Elton John's sons?: \n"), 
                 ("\nWhat is Rihanna's real name?: \n"), 
                 ("\nWhich pop star accidentally set fire to her home gym with candles?: \n"),
                 ("\nWhich pop star was Judge Judy's neighbor?: \n"),
                 )

        options = (("A. Chicago", "B. East", "C. Palm", "D. North"),
               ("A. Mariah Carey", "B. Tina Turner", "C. Lady Gaga", "D. Madonna"),
               ("A. Rihanna Felty", "B. Robyn Fenty", "C. Robin Dern", "D. Rachel Feaner"),
               ("A. Lady Gaga", "B. Rihanna", "C. Miley Cyrus", "D. Britney Spears"),
               ("A. Justin Bieber", "B. Adele", "C. Taylor Swift", "D. Bruno Mars"),
    )

        answers = ("B", "C", "B", "D", "A")
        quiz(questions, options, answers, topic_choice)

# General Knowledge Quiz

    elif topic_choice == "5":
        questions = (("\nWhat name is NOT one of Kim or Kanye's children?: \n"), 
                 ("\nWhich pop star is the godmother of both of Elton John's sons?: \n"), 
                 ("\nWhat is Rihanna's real name?: \n"), 
                 ("\nWhich pop star accidentally set fire to her home gym with candles?: \n"),
                 ("\nWhich pop star was Judge Judy's neighbor?: \n"),
                 )

        options = (("A. Chicago", "B. East", "C. Palm", "D. North"),
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
    print("[purple]-----------------------------[/purple]")
    print("     :dart:  [bold blue]HIGH SCORES[/bold blue]  :dart: ")
    print("[purple]-----------------------------[/purple]\n")
    file_name = "list.csv"

    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            # reader.__next__()

            music_highscores = []
            history_highscores = []
            cities_highscores = []
            cs_highscores = []
            gk_highscores = []

            for i in reader:
                if i[0] == "1":
                    music_highscores.append(float(i[1]))
                elif i[0] == "2":
                    history_highscores.append(float(i[1]))
                elif i[0] == "3":
                    cities_highscores.append(float(i[1]))
                elif i[0] == "4":
                    cs_highscores.append(float(i[1]))
                elif i[0] == "5":
                    gk_highscores.append(float(i[1]))

            music_highscores.sort(reverse=True)
            history_highscores.sort(reverse=True)   
            cities_highscores.sort(reverse=True)
            cs_highscores.sort(reverse=True)
            gk_highscores.sort(reverse=True)

            
            print("   :microphone:[bold blue]MUSIC[/bold blue]    :microphone")
            if not music_highscores:
                print("You have not attempted the Music Quiz yet.")
            else:
                print(f"Your highest Music Quiz score is {music_highscores[0]:.4f}!")
            if not music_highscores[1]: 
                print("You have only attempted this quiz once.")
            else:
                print(f"Your second highest score is {music_highscores[1]:.4f}")
            if not music_highscores[2]: 
                print("You have only attempted this quiz twice.")
            else:
                print(f"Your second highest score is {music_highscores[2]:.4f}")

            print("[purple]-----------------------------[/purple]")
            print("    :book:  [bold red]HISTORY  [/bold red] :book:")
            print("[purple]-----------------------------[/purple]")
            if not history_highscores:
                print("You have not attempted the History Quiz yet.")
            else:
                print(f"Your highest History Quiz score is {history_highscores[0]:.4f}!")
            if not history_highscores[1]: 
                print("You can only attempted this quiz once.")
            else:
                print(f"Your second highest score is {history_highscores[1]:.4f}")
            if not history_highscores[2]: 
                print("You can only attempted this quiz twice.")
            else:
                print(f"Your second highest score is {history_highscores[2]:.4f}")

            print("[purple]-----------------------------[/purple]")
            print("  :house: [bold red]CAPITAL CITIES[/bold red] :house:")
            print("[purple]-----------------------------[/purple]")
            if not cities_highscores:
                print("You have not attempted the Capital Cities quiz yet.")
            else:
                print(f"Your highest Capital Cities Quiz score is {cities_highscores[0]:.4f}!")
            if not cities_highscores[1]: 
                print("You can only attempted this quiz once.")
            else:
                print(f"Your second highest score is {cities_highscores[1]:.4f}")
            if not cities_highscores[2]: 
                print("You can only attempted this quiz twice.")
            else:
                print(f"Your second highest score is {cities_highscores[2]:.4f}")

            print("[purple]-----------------------------[/purple]")
            print("  :dvd: [bold red]COMPUTER SCIENCE[/bold red] :dvd:")
            print("[purple]-----------------------------[/purple]")
            if not cs_highscores:
                print("You have not attempted for the Computer Science quiz yet.")
            else: 
                print(f"Your highest Computer Science Quiz score is {cs_highscores[0]:.4f}!")
            if not cs_highscores[1]: 
                print("You can only attempted this quiz once.")
            else:
                print(f"Your second highest score is {cs_highscores[1]:.4f}")
            if not cs_highscores[2]: 
                print("You can only attempted this quiz twice.")
            else:
                print(f"Your second highest score is {cs_highscores[2]:.4f}")

            print("[purple]-----------------------------[/purple]")
            print("  :microbe: [bold red]GENERAL KNOWLEDGE[/bold red] :microbe:")
            print("[purple]-----------------------------[/purple]")
            if not gk_highscores:
                print("You have not attempted the General Knowledge Quiz yet.")
            else:
                print(f"Your highest General Knowledge Quiz score is {gk_highscores[0]:.4f}!\n")
            if not gk_highscores[1]: 
                print("You can only attempted this quiz once.")
            else:
                print(f"Your second highest score is {gk_highscores[1]:.4f}")
            if not gk_highscores[2]: 
                print("You can only attempted this quiz twice.")
            else:
                print(f"Your second highest score is {gk_highscores[2]:.4f}")

            input("Press any key for main menu: \n")
    except: 
        print("Sorry, there's no quiz scores to show right now.\n")
        input("Press any key for main menu: \n")
    

def random_quiz():
    rand_quiz = random.randint(1, 5)
    quiz_topics(rand_quiz)
    

def create_new():
    print("new")

