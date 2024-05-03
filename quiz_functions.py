# Stanard Library Imports
import csv
import random
from operator import itemgetter

# Related third party imports
from rich import print
from rich.console import Console
from rich.table import Table
# from rich.style import Style

# Local application/library specific imports
from quizzes import quiz


# Quiz Topics Menu and Quiz data function
def quiz_topics(username, rand_quiz=None):
    try:
        # Create console variable for the rich table
        console = Console()

        # Table columns with selection and topic headings
        table = Table(
            title=":book:  QUIZ TOPICS  :book:",
            style="purple",
            show_lines=True,
            title_style="bold white on purple")
        table.add_column("Selection", style="bold cyan", justify="center")
        table.add_column("Topic", style="bold cyan", justify="center")
        table.add_column("", style="green", justify="center")

        # Table rows with quiz topics and number selects
        table.add_row("1", "Music", ":microphone:")
        table.add_row("2", "History", ":book:")
        table.add_row("3", "Capital Cities", ":house:")
        table.add_row("4", "Computer Science", ":dvd:")
        table.add_row("5", "General Knowledge", ":microbe:")
        table.add_row(
            "6",
            "[bright_red]Return to Main Menu[/bright_red]",
            ":back:")

        # If random quiz has not been called print the table
        if rand_quiz is None:
            console.print(table)

        # If random quiz has not been called asked user for selection
        if rand_quiz is None:
            topic_choice = input("\nPlease enter your selection: \n")

        else:
            # Random quiz has been called and rand_quiz integar ='s
            # topic_choice
            topic_choice = str(rand_quiz)

    # Music Quiz if topic choice ='s 1
        if topic_choice == "1":
            # Questions
            questions = (
                ("\nHow many band members are there in the Rolling Stones?: \n"),
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
            # Options
            options = (
                ("A. 4", "B. 7", "C. 5", "D. 6"),
                ("A. A Tribe Called Quest", "B. Wutang", "C. OutKast", "D. NWA"),
                ("A. Rihanna Felty", "B. Robyn Fenty", "C. Robin Dern", "D. Rachel Feaner"),
                ("A. Trumpet", "B. Saxophone", "C. Guitar", "D. Piano"),
                ("A. Johnny Thunders", "B. Jonny Vicious", "C. Edgar Emerald", "D. Sid Vicious"),
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
            # Answers
            answers = (
                "C",
                "C",
                "B",
                "A",
                "D",
                "B",
                "A",
                "A",
                "C",
                "D",
                "B",
                "A",
                "C",
                "B",
                "A"
                )
            # Call quiz function to run quiz
            quiz(questions, options, answers, topic_choice, username)

    # History Quiz if topic choice ='s 2
        elif topic_choice == "2":

            # Questions
            questions = (
                ("\nWhat year was the Berlin Wall built?: \n"),
                ("\nWho was the first person in space?: \n"),
                ("\nIn what year was Napoleon defeated at Waterloo?: \n"),
                ("\nWhich of these conflicts involved two US allies fighting against each other?: \n"),
                ("\nWhich Roman Emperor legalised Christianity in the Roman Empire?: \n"),
                ("\nWhich disease has killed the most humans throughout history?: \n"),
                ("\nThe siege of Kohima was part of which conflict?: \n"),
                ("\nWhen was the Declaration of Independence signed?: \n"),
                ("\nThe United States bought Alaska from which country?: \n"),
                ("\nWhere was Martin Luther King, Jr. born?: \n"),
                ("\nAustralia's Parliament met in which city from 1901 to 1927?: \n"),
                ("\nWhere did the Rum Rebellion take place?: \n"),
                ("\nWhere was Ned Kelly captured after a final shootout with police?: \n"),
                ("\nWhich country did Germany invade to kickstart World War II?: \n"),
                ("\nMartin Luther King Jr. was assassinated in which US state?: \n"),
                ("\nWho discovered penicillin?: \n"),
            )

            # Options
            options = (
                ("A. 1948", "B. 1961", "C. 1957", "D. 1964"),
                ("A. John Glenn", "B. Vladimir Komarov", "C. Neil Armtsrong", "D. Yuri Gagarin"),
                ("A. 1815", "B. 1835", "C. 1861", "D. 1798"),
                ("A. The Korean War", "B. The Crimean War", "C. The invasion of the Falklands", "The Boer War"),
                ("A. Claudius", "B. Vaspasian", "C. Hadrian", "D. Constantine"),
                ("A. Plague", "B. Tuberculosis", "C. Influenza", "D. Smallpox"),
                ("A. WW2", "B. WW1", "C. Korean War", "D. Vietnam War"),
                ("A. 1804", "B. 1745", "C. 1723", "D. 1776"),
                ("A. Norway", "B. Finland", "C. Russia", "D. Switzerland"),
                ("A. North Carolina", "B. New York", "C. Michigan", "D. Georgia"),
                ("A. Sydney", "B. Melbourne", "C. Canberra", "D. Adelaide"),
                ("A. Hobart", "B. Adelaide", "C. Sydney", "D. Melbourne"),
                ("A. Glenrowan", "B. Jerilderie", "C. Greta", "D. Beveridge"),
                ("A. France", "B. Ukraine", "C. Poland", "D. Belarus"),
                ("A. Texas", "B. Louisiana", "C. Alabama", "D. Tennessee"),
                ("A. Geoffery Bennet", "B. John Daniels", "C. Alexander Fleming", "D. Thomas Hoover"),
            )

            # Answers
            answers = (
                    "B", 
                    "D", 
                    "B", 
                    "C", 
                    "D", 
                    "B", 
                    "A", 
                    "D",
                    "C", 
                    "D", 
                    "B", 
                    "C", 
                    "A", 
                    "C", 
                    "D", 
                    "C"
                    )

            # Call quiz function to run quiz
            quiz(questions, options, answers, topic_choice, username)

    # Capital Cities Quiz if topic choice ='s 3
        elif topic_choice == "3":

            # Questions
            questions = (
                ("\nWhat is the capital of Romania?: \n"),
                ("\nWhat is the capital of Botswana?: \n"),
                ("\nWhat is the capital of Kosovo?: \n"),
                ("\nWhat is the capital of Bosnia & Herzegovina?: \n"),
                ("\nWhat is the capital of Mauritania?: \n"),
                ("\nWhat is the capital of Belize?: \n"),
                ("\nWhat is the capital of Zambia?: \n"),
                ("\nWhat is the capital of Senegal?: \n"),
                ("\nWhat is the capital of Tuvalu?: \n"),
                ("\nWhat is the capital of Oman?: \n"),
                ("\nWhat is the capital of Angola?: \n"),
                ("\nWhat is the capital of Afghanistan?: \n"),
                ("\nWhat is the capital of Zimbabwe?: \n"),
                ("\nWhat is the capital of Paraguay?: \n"),
                ("\nWhat is the capital of Cameroon?: \n"),
            )

            # Options
            options = (
                ("A. Bucharest", "B. Monrovia", "C. Dhiresj", "D. Basseterre"),
                ("A. Lusaka", "B. Gaborone", "C. Kampala", "D. Edali"),
                ("A. Monrovia", "B. Khartoum", "C. Port-Vila", "D. Pristina"),
                ("A. Sarajenko", "B. Bogota", "C. Sarajevo", "D. Beotojka"),
                ("A. Nouakchott", "B. Port Louis", "C. Bishkek", "D. Jerusalem"),
                ("A. Vaduz", "B. Libreville", "C. Belmopan", "D. Port Louis"),
                ("A. Damascus", "B. Pristina", "C. Sarajevo", "D. Lusaka"),
                ("A. Dakar", "B. Kinshasha", "C. Lome", "D. Bogota"),
                ("A. San Jose", "B. Funafuti", "C. Tallin", "D. Fufeli"),
                ("A. Muscat", "B. Lilongwe", "C. Lusaka", "D. Port Louis"),
                ("A. Honiara", "B. Castries", "C. Luanda", "D. Damascus"),
                ("A. Kampala", "B. Kabul", "C. Basseterre", "D. Ouagadougou"),
                ("A. Zagreb", "B. Bern", "C. Kinshasha", "D. Harare"),
                ("A. Asuncion", "B. Nairobi", "C. Nassau", "D. Bangui"),
                ("A. Quito", "B. Nairobi", "C. Nassau", "D. Yaounde"),
            )

            # Answers
            answers = (
                "A",
                "B",
                "D",
                "C",
                "A",
                "C",
                "C",
                "D",
                "B",
                "A",
                "C",
                "B",
                "D",
                "A",
                "D"
            )

            # Call quiz function to run quiz
            quiz(questions, options, answers, topic_choice, username)

    # Computer Science Quiz if topic choice ='s 4
        elif topic_choice == "4":

            # Questions
            questions = (
                ("\nWhich is considered to be the computer's short-term memory?: \n"),
                ("\nWhat is the brain of the computer?: \n"),
                ("\nWhat allows multiple programs to run on a computer?: \n"),
                ("\nWhen was the world wide web invented?: \n"),
                ("\nEverything physical in a computer is attached to the...?: \n"),
                ("\nInformation that is broken down into small chunks before it is sent to another computer are called...: \n"),
                ("\nWhat does GUI stand for....?: \n"),
                ("\nThe Second Generation Computer used …?: \n"),
                ("\nWhich among the following works faster?: \n"),
                ("\n……………. is a set of finite elements that interconnects different elements of computer systems.: \n"),
                ("\nThe .com used frequently in website url can be expressed as …: \n"),
                ("\nWhat is the full form of the CPU?: \n"),
                ("\nWhich of the following is the binary representation of 4 5/8?: \n"),
                ("\nA numeric value used to identify a memory cell?: \n"),
                ("\nA means of encoding text in which each symbol is represented by 16 bits: \n"),
                ("\nA numeric value used to identify a memory cell?: \n"),
                ("\nA digital circuit capable of holding a single digit: \n"),
                ("\nWhich of the following bit patterns represents the value 5 in twos complement notation?: \n"),
            )

            # Options
            options = (
                ("A. Rim", "B. Rom", "C. Ram", "D. Rem"),
                ("A. CPU", "B. NIC", "C. Motherboard", "D. Memory"),
                ("A. NIC", "B. API", "C. OS", "D. GUI"),
                ("A. 1975", "1984", "C. 1991", "D. 1989"),
                ("A. Hard drive", "B. CPU", "C. Monitor", "D. Motherboard"),
                ("A. Letters", "B. Packets", "C. Packages", "D. Messages"),
                ("A. Graphical User Interface", "B. Graphical User Interim", "C. Graphical Usage Interface ", "D. Geographical User Interface"),
                ("A. Chip", "B. Vacuum Tube", "C. Transistors", "D. Integrated Circuitry"),
                ("A. Ram", "B. Cache", "C. Register", "D. Rom"),
                ("A. Starfish", "B. Nodes", "C. Junctions", "D. Mesh"),
                ("A. Corporation", "B. Commercial", "C. Common", "D. Conditional"),
                ("A. Central Program Unit", "B. Central Programming Unit", "C. Central Processing Unit", "D. Centralised Processing Unit"),
                ("A. 100.101", "B. 110.101", "C. 10.011", "D. 100.110"),
                ("A. Address", "B. Hexadecimal Notation", "C. ", "D. Bit"),
                ("A. ISO", "B. ASCII", "C. LZW", "D. Unicode"),
                ("A. Pixel", "B. Bit", "C. Flip Flop", "D. Key Field"),
                ("A. 11111011", "B. 00000101", "C. 11110011", "D. 00011010"),
            )

            # Answers
            answers = (
                "C", 
                "A", 
                "C", 
                "D", 
                "C", 
                "B", 
                "A", 
                "C", 
                "B", 
                "D", 
                "B", 
                "C", 
                "B", 
                "A", 
                "D", 
                "C", 
                "B"
            )

            # Call quiz function to run quiz
            quiz(questions, options, answers, topic_choice, username)

    # General Knowledge Quiz if topic choice ='s 5
        elif topic_choice == "5":

            # Questions
            questions = (
                ("\nIn which year was television invented?: \n"),
                ("\nIn which city was US President John F. Kennedy assassinated?: \n"),
                ("\nKorea was split into North Korea and South Korea at the conclusion of which war?: \n"),
                ("\nWho invented the first successful aeroplane?: \n"),
                ("\nHow many days in a week were there in ancient Roman times?"),
                ("\nWhat did the famous Hollywood sign originally say when it was built in 1923?: \n"),
                ("\nIn which ocean did the Titanic sink??: \n"),
                ("\nIn which year was the Berlin wall removed?: \n"),
                ("\nThe first person to travel into space was from which country?: \n"),
                ("\nWhere was the first modern Summer Olympic Games held?: \n"),
                ("\nHow long did the war between England and Zanzibar last?: \n"),
                ("\nHow long did the 100 year war last?: \n"),
                ("\nIn which year did Hitler commit suicide?: \n"),
                ("\nIn which year was John F. Kennedy assassinated?: \n"),
                ("\nGreenland was a colony of which country until 1981?: \n"),
            )

            # Options
            options = (
                ("A. 1927", "B. 1941", "C. 1907", "D. 1953"),
                ("A. New York", "B. Las Vegas", "C. Washington DC", "D. Dallas"),
                ("A. WW1", "B. WW2", "C. Korean War", "D. Vietnam War"),
                ("A. Karl Benz", "B. Guglielmo Marconi", "C. John Logie Baird", "D. Orville and Wilbur Wright"),
                ("A. 5", "B. 9", "C. 6", "D. 8"),
                ("A. HOLLYWOODVILLE", "B. HOLLYWOOD LA", "C. HOLLYWOOD HILLS", "D. HOLLYWOODLAND"),
                ("A. Indian", "B. Atlantic", "C. Arctic", "D. Pacific"),
                ("A. 1989", "B. 1988", "C. 1992", "D. 1991"),
                ("A. Amercia", "B. Germany", "C. Ukraine", "D. Russia"),
                ("A. Athens", "B. Rome", "C. Paris", "D. London"),
                ("A. 2 days", "B. Between 5 & 2 hours", "C. 22 minutes", "D. Between 38 & 45 minutes"),
                ("A. 100", "B. 116", "C. 108", "D. 99"),
                ("A. 1944", "B. 1946", "C. 1945", "D. 1947"),
                ("A. 1961", "B. 1963", "C. 1965", "D. 1967"),
                ("A. Denmark", "B. Norway", "C. Russia", "D. Switzerland"),
            )

            # Answers
            answers = (
                "A",
                "D",
                "B",
                "D",
                "D",
                "D",
                "B",
                "A",
                "D",
                "A",
                "D",
                "B",
                "C",
                "B",
                "A"
                )

            # Call quiz function to run quiz
            quiz(questions, options, answers, topic_choice, username)

        # Return to Main Menu
        elif topic_choice == "6":
            return

        else:
            # Error handling if invalid input is entered
            print("Please only input corresponding topic numbers shown above.\n")
            input("Enter any key to return to quiz topics menu\n")
            quiz_topics(username)

    except BaseException:
        # Unexpected Error Handling
        print("Oops! Something seems to be not working, please try again.")


# High Scores Board Function
def top_scores():
    try:
        console = Console()

        # Create a rich table with 1st, 2nd and 3rd columns
        table = Table(
            title=":trophy: High Scores :trophy:",
            style="bold purple",
            show_lines=True,
            title_style="bold white on purple")
        table.add_column("Category", style="cyan", justify="left")
        table.add_column("1st Place", style="green", justify="center")
        table.add_column("2nd Place", style="red", justify="center")
        table.add_column("3rd Place", style="yellow", justify="center")

        # Assign variable file_name to list.csv so that it can be opened
        file_name = "list.csv"

        try:
            # Open csv file holding the scores in read mode and creat 5 new
            # lists
            with open(file_name, "r") as f:
                reader = csv.reader(f)
                music_highscores = []
                history_highscores = []
                cities_highscores = []
                cs_highscores = []
                gk_highscores = []

                # Loop through csv list and append data row based on topic
                # number
                for i in reader:
                    if i[0] == "1":
                        music_highscores.append((i[2], float(i[1])))
                    elif i[0] == "2":
                        history_highscores.append((i[2], float(i[1])))
                    elif i[0] == "3":
                        cities_highscores.append((i[2], float(i[1])))
                    elif i[0] == "4":
                        cs_highscores.append((i[2], float(i[1])))
                    elif i[0] == "5":
                        gk_highscores.append((i[2], float(i[1])))

                # Sort the new lists in reverse order by scores or x[1]
                # lambda did not adhere to the pep 8 styling
                # So itemgetter(1) was used to access scores, then sort and
                # reverse

                # music_highscores.sort(key=lambda x: x[1], reverse=True)
                music_highscores.sort(key=itemgetter(1), reverse=True)

                # history_highscores.sort(key=lambda x: x[1], reverse=True)
                history_highscores.sort(key=itemgetter(1), reverse=True)

                # cities_highscores.sort(key=lambda x: x[1], reverse=True)
                cities_highscores.sort(key=itemgetter(1), reverse=True)

                # cs_highscores.sort(key=lambda x: x[1], reverse=True)
                cs_highscores.sort(key=itemgetter(1), reverse=True)

                # gk_highscores.sort(key=lambda x: x[1], reverse=True)
                gk_highscores.sort(key=itemgetter(1), reverse=True)

                # Add rows to the table and display index [0] username and index [1]
                # score for the first three itertaions [:3]
                table.add_row("[bold]Music[/bold] :microphone:", *
                              [f"{score[0]} - {score[1]:.2f}" for score in music_highscores[:3]])
                table.add_row("[bold]History[/bold] :book:", *
                              [f"{score[0]} - {score[1]:.2f}" for score in history_highscores[:3]])
                table.add_row("[bold]Capital Cities[/bold] :house:", *
                              [f"{score[0]} - {score[1]:.2f}" for score in cities_highscores[:3]])
                table.add_row("[bold]Computer Science[/bold] :dvd:", *
                              [f"{score[0]} - {score[1]:.2f}" for score in cs_highscores[:3]])
                table.add_row("[bold]General Knowledge[/bold] :microbe:",
                              *[f"{score[0]} - {score[1]:.2f}" for score in gk_highscores[:3]])

                # Print the table
                console.print(table)

                # Input holder so
                input("Press any key for main menu: \n")

        except BaseException:
            # If the csv file holding the scores has not been created yet
            print("Sorry, there's no quiz scores to show right now.\n")
            input("Press any key for main menu: \n")

    except BaseException:
        # Unexpected Error Handling
        print("Oops! Something seems to be not working, please try again.")


# Random Quiz Function
def random_quiz(username):
    try:
        # Use random package to return a integer between 1 and 5
        rand_quiz = random.randint(1, 5)
        # quiz_topics function passing the rand_quiz integer
        quiz_topics(username, rand_quiz)
    except BaseException:
        # Unexpected Error Handling
        print("Oops! Something seems to be not working, please try again.")


# Instructions Function
def instructions():
    try:
        print("new")

    except BaseException:
        # Unexpected Error Handling
        print("Oops! Something seems to be not working, please try again.")
