# System Packages
import os.path
import csv
import random

# External Packages
# from colorama import Fore, Style, Back
from rich import print 
from rich.console import Console
from rich.table import Table
from rich.style import Style


# App functions
from quizzes import quiz

def quiz_topics(rand_quiz=None):
    
    # print("[purple]-----------------------------[/purple]")
    # print("    :microbe:  [bold red]QUIZ TOPICS  [bold red] :microbe:")
    # print("[purple]-----------------------------[/purple]\n")
    # print("1. Enter 1 - for [bold blue]Music[/bold blue] :microphone:")
    # print("2. Enter 2 - for [bold green]History[/bold green] :book:")
    # print("3. Enter 3 - for [bold magenta]Capital Cities[/bold magenta] :house:")
    # print("4. Enter 4 - for [bold yellow]Computer Science[/bold yellow] :dvd:")
    # print("5. Enter 5 - for [bold red]General Knowledge[/bold red] :microbe:")
    # print("6. Enter 6 - to return to [bold black]main menu[/bold black]")
    console = Console()

    table = Table(title=":book:  QUIZ TOPICS  :book:", style="purple", show_lines=True, title_style="bold white on purple")
    table.add_column("Selection", style="bold cyan", justify="center")
    table.add_column("Topic", style="bold cyan", justify="center")
    table.add_column("", style="green", justify="center")

    table.add_row("1", "Music", ":microphone:")
    table.add_row("2", "History", ":book:")
    table.add_row("3", "Capital Cities", ":house:")
    table.add_row("4", "Computer Science", ":dvd:")
    table.add_row("5", "General Knowledge", ":microbe:")
    table.add_row("6", "[bright_red]Return to Main Menu[/bright_red]", ":back:")

    if rand_quiz == None:
        console.print(table)

    if rand_quiz is None:
        topic_choice = input("\nPlease enter your selection: \n")
    else: 
        topic_choice = str(rand_quiz)

    

# Music Quiz

    if topic_choice == "1": 
        
        questions = (("\nHow many band members are there in the Rolling Stones?: \n"), 
                 ("\nArtist Andre 3000 is a rapper in what well-known music group?: \n"), 
                 ("\nWhat is Rihanna's real name?: \n"), 
                 ("\nArtist Miles Davis played the what?: \n"),
                 ("\nThe name of the lead singer in the Sex Pistols is?: \n"),
                 ("\nWhat is Freddy Mercury's real name?:\n"),
                 ("\nWhat is the best selling album of all time?: \n"),
                 ("\nWhy was the leads singer of Led Zeppelin?: \n"),
                 ("\nWho is referred to as the queen of pop?: \n"),
                 ("\nWho is the song 'Could you be loved' by?: \n"),
                 ("\nWhich of these name aren't of a member from the Beatles?: \n"),
                 ("\nIn The Big Lebowski, The Dude can't stand which band?: \n"),
                 ("\nWhich classical composer was deaf?: \n"),
                 ("\nWhere was Tupac Shakur born?: \n"),
                 ("\nWhich of these names aren't a member of NWA?: \n"),
                 )

        options = (("A. 4", "B. 7", "C. 5", "D. 6"),
               ("A. A Tribe Called Quest", "B. Wutang", "C. OutKast", "D. NWA"),
               ("A. Rihanna Felty", "B. Robyn Fenty", "C. Robin Dern", "D. Rachel Feaner"),
               ("A. Trumpet", "B. Saxophone", "C. Guitar", "D. Piano"),
               ("A. Johnny Garbage", "B. Jonny Vicious", "C. Edgar Emerald", "D. Sid Vicious"),
               ("A. Amein Selara", "B. Farrokh Bulsara", "C. Frederick Merise", "D. Elsai Kilara"),
               ("A. Michael Jackson - Thriller", "B. The Beatles - The White Album", "C. ACDC - Back in Black", "D. Pink Floyd - The Dark Side of the Moon"),
               ("A. Robert Plant", "B. Jimmy Page", "C. John Bonham", "D, John Paul Jones"),
               ("A. Kylie Monogue", "B. Lady Gaga", "C. Madonna", "D. Beyonce"),
               ("A. The Beatles", "B. Michael Jackson", "C. Whitney Houston", "D. Bob Marley"),
               ("A. Paul McCartney", "B. David Blight", "C. John Lennon", "D. George Harrison"),
               ("A. The Eagles", "B. Santana", "C. Led Zeppelin", "D. Pink Floyd"),
               ("A. Mozart", "B. Vivaldi", "C. Beethoven", "D. Bach"),
               ("A. Detroit", "B. New York", "C. Los Angeles", "D. Georgia"),
               ("A. Method Man", "B. DJ Yella", "C. Snoop Dogg", "D. MC Ren"),

    )

        answers = ("C", "C", "B", "A", "D", "B", "A", "A", "C", "D", "B", "A", "C", "B", "A")
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
        questions = (("\nHow many band members are in the rolling stones?: \n"), 
                 ("\nRapper Andre 3000 is in what music group?: \n"), 
                 ("\nWhat is Rihanna's real name?: \n"), 
                 ("\nWhich pop star accidentally set fire to her home gym with candles?: \n"),
                 ("\nWhich pop star was Judge Judy's neighbor?: \n"),
                 )

        options = (("A. 3", "B. 6", "C. 5", "D. 4"),
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
        print("Please only input corresponding topic numbers shown above.\n")
        input("Enter any key to return to quiz topics menu\n")
        quiz_topics()


def top_scores():
    console = Console()

    # Create a rich table
    table = Table(title=":trophy: High Scores :trophy:", style="bold purple", show_lines=True, title_style="bold white on purple")
    table.add_column("Category", style="cyan", justify="left")
    table.add_column("1st Place", style="green", justify="center")
    table.add_column("2nd Place", style="red", justify="center")
    table.add_column("3rd Place", style="yellow", justify="center")

    file_name = "list.csv"

    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
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

            # Add rows to the table
            table.add_row("[bold]Music[/bold] :microphone:", *[f"{score:.2f}" for score in music_highscores[:3]])
            table.add_row("[bold]History[/bold] :book:", *[f"{score:.2f}" for score in history_highscores[:3]])
            table.add_row("[bold]Capital Cities[/bold] :house:", *[f"{score:.2f}" for score in cities_highscores[:3]])
            table.add_row("[bold]Computer Science[/bold] :dvd:", *[f"{score:.2f}" for score in cs_highscores[:3]])
            table.add_row("[bold]General Knowledge[/bold] :microbe:", *[f"{score:.2f}" for score in gk_highscores[:3]])

            # Print the table
            console.print(table)

            input("Press any key for main menu: \n")
    except: 
        print("Sorry, there's no quiz scores to show right now.\n")
        input("Press any key for main menu: \n")
# def top_scores():
#     print("[purple]-----------------------------[/purple]")
#     print("     :dart:  [bold blue]HIGH SCORES[/bold blue]  :dart: ")
#     print("[purple]-----------------------------[/purple]\n")
#     file_name = "list.csv"

#     try:
#         with open(file_name, "r") as f:
#             reader = csv.reader(f)
#             # reader.__next__()

#             music_highscores = []
#             history_highscores = []
#             cities_highscores = []
#             cs_highscores = []
#             gk_highscores = []

#             for i in reader:
#                 if i[0] == "1":
#                     music_highscores.append(float(i[1]))
#                 elif i[0] == "2":
#                     history_highscores.append(float(i[1]))
#                 elif i[0] == "3":
#                     cities_highscores.append(float(i[1]))
#                 elif i[0] == "4":
#                     cs_highscores.append(float(i[1]))
#                 elif i[0] == "5":
#                     gk_highscores.append(float(i[1]))

#             music_highscores.sort(reverse=True)
#             history_highscores.sort(reverse=True)   
#             cities_highscores.sort(reverse=True)
#             cs_highscores.sort(reverse=True)
#             gk_highscores.sort(reverse=True)

#             # Music High Scores
#             print("[purple]-----------------------------[/purple]")
#             print("       :microphone:   [bold red]MUSIC  [/bold red]:microphone:")
#             print("[purple]-----------------------------[/purple]")
#             if not music_highscores:
#                 print("No attempts")
#             else:
#                 print(f":trophy: - [bold underline]{music_highscores[0]:.2f}[/bold underline]\n")
#             if len(music_highscores) >= 2: 
#                 print(f"[green]2 - {music_highscores[1]:.2f}[/green]")
            
#             if len(music_highscores) >= 3: 
#                 print(f"[purple]3 - {music_highscores[2]:.2f}[/purple]")
            
#             # History High Scores
#             print("[purple]-----------------------------[/purple]")
#             print("      :book:   [bold red]HISTORY  [/bold red]:book:")
#             print("[purple]-----------------------------[/purple]")
#             if not history_highscores:
#                 print("No attempts")
#             else:
#                 print(f"       :trophy: - [bold]{history_highscores[0]:.4f}[/bold]\n")
#             if len(history_highscores) >= 2: 
#                 print(f"     [green]Second - {history_highscores[1]:.4f}[/green]")
            
#             if len(history_highscores) >= 3: 
#                 print(f"     [purple]Third - {history_highscores[2]:.4f}[/purple]")
            

#             # Capital Cities High Scores
#             print("[purple]-----------------------------[/purple]")
#             print("    :house: [bold red]CAPITAL CITIES[/bold red]  :house:")
#             print("[purple]-----------------------------[/purple]")
#             if not cities_highscores:
#                 print("No attempts")
#             else:
#                 print(f"       :trophy: - {cities_highscores[0]:.4f}")
#             if len(cities_highscores) >= 2: 
#                 print(f"     Second - {cities_highscores[1]:.4f}")
            
#             if len(cities_highscores) >= 3: 
#                 print(f"     Third - {cities_highscores[2]:.4f}")
            

#             # Computer Science High Scores
#             print("[purple]-----------------------------[/purple]")
#             print("   :dvd: [bold red]COMPUTER SCIENCE[/bold red]  :dvd:")
#             print("[purple]-----------------------------[/purple]")
#             if not cs_highscores:
#                 print("No attempts")
#             else: 
#                 print(f"       :trophy: - {cs_highscores[0]:.4f}!\n")
#             if len(cs_highscores) >= 2: 
#                 print(f"     Second - {cs_highscores[1]:.4f}")
            
#             if len(cs_highscores) >= 3: 
#                 print(f"     Third - {cs_highscores[2]:.4f}")
            

#             # General Knowledge High Scores
#             print("[purple]-----------------------------[/purple]")
#             print("   :microbe: [bold red]GENERAL KNOWLEDGE[/bold red]  :microbe:")
#             print("[purple]-----------------------------[/purple]")
#             if not gk_highscores:
#                 print("You have not attempted the General Knowledge Quiz yet.")
#             else:
#                 print(f"       :trophy: - {gk_highscores[0]:.4f}\n")
#             if len(gk_highscores) >= 2: 
#                 print(f"     Second - {gk_highscores[1]:.4f}")
            
#             if len(gk_highscores) >= 3: 
#                 print(f"     Third - {gk_highscores[2]:.4f}")
            

#             input("Press any key for main menu: \n")
#     except: 
        
#         print("Sorry, there's no quiz scores to show right now.\n")
#         input("Press any key for main menu: \n")
    

def random_quiz():
    rand_quiz = random.randint(1, 5)
    quiz_topics(rand_quiz)
    

def create_new():
    print("new")

