# System Packages
import os.path
import csv
import random
import time
from time import sleep

# External Packages
# from colorama import Fore, Style, Back
from rich import print
from rich.progress import track
# from rich.prompt import Prompt

# App functions


# Function to calculate total points based on score and time
def calculate_points(score, total_questions, total_time):
    try:
        # Score points: 50 points for each correct answer
        score_points = score * 50
        
        # Time points: 1 point for each second saved
        max_time = total_questions * 30  # Assuming 30 seconds per question
        time_points = (max_time - total_time) if total_time < max_time else 0
        
        # Total points: sum of score points and time points
        total_points = score_points + time_points
        return total_points
    
    # Unexpected Error Handling    
    except: 
        print("Oops! Something seems to be not working, please try again.")


# Function that runs and displays the quiz data and results
def quiz(questions, options, answers, topic_choice, username):
    try:
        try:

            # Rich get ready bar 
            def process_data():
                sleep(0.02)
            for _ in track(range(100), description='[green]Get ready!'):
                process_data()
            print()

        except: 
            # Unexpected Error Handling
            print("Oops! Something seems to be not working, please try again.")
    
        # Zip questions, options and answers so that random treats their index positons as the same when shuffling
        combined = list(zip(questions, options, answers))
        random.shuffle(combined)
        shuffled_questions, shuffled_options, shuffled_answers = zip(*combined)


        # Start time time stamp
        start_time = time.time()
        
        # Assign new list to variable file_name
        file_name = "list.csv"

        # If the file doesn't exist we must create it
        # Add topic and score headings and then close it the file
        if (not os.path.isfile(file_name)):
            high_scores = open(file_name, "w")
            high_scores.write("topic,score,username\n")
            high_scores.close()
        
        # Correct Answers score counter starting at 0
        score = 0

        # A black list to append user guesses per question
        guesses = []

        # Question number counter starting at 0
        question_num = 0

        # Loop through each question in question_num counter index and print
        # Loop through each option in question_num counter index and print 
        for question in shuffled_questions:
            print("[purple]-----------------------------[/purple]")
            print(question)
            for option in shuffled_options[question_num]:
                print(option)

            # User input their option answer as A, B, C or D
            # If question in question_num index guess == answer in question_num counter index + 1 score
            # Finally question_num + 1 for next question iteration
            guess = input( "\nEnter (A, B, C, D): \n").upper()
            guesses.append(guess)

            if guess == shuffled_answers[question_num]:
                score += 1
                print("[bold green]Correct![/bold green]")

            elif guess not in ["A", "B", "C", "D"]:
                print(f"{guess} is not a valid answer!")

            else: 
                print("[bold red]Incorrect![bold red]")
                print(f"[bold green]{shuffled_answers[question_num]} is the correct answer.[/bold green]")
            question_num += 1

        # End time - calculate total time
        end_time = time.time()
        total_time = end_time - start_time
        
        # Print results banner
        print("[purple]-----------------------------[purple]")
        print("       [bold bright_red]   RESULTS       [/bold bright_red]     ")
        print("[purple]-----------------------------[purple]\n")
        
        # Correct answers
        print("[green bold]Answers: [/green bold]", end=" ")
        for answer in answers:
            print(answer, end=" ")
        
        # User guesses
        print("\n[bold blue]Guesses: [/bold blue]", end=" ")
        for guess in guesses:
            print(guess, end=" ")
        
        # Total score %
        print("")
        score = int(score / len(shuffled_questions) * 100)
        print(f"\nYour score is {score}%")
        print(f"Total time taken: {total_time:.2f} seconds\n")

        # Calculate total points based on score and time
        total_points = calculate_points(score, len(shuffled_questions), total_time)
        print(f"Total points: [bold red]{total_points:.2f}[/bold red]\n")

        # Append topic and total points to 'list.csv'
        with open(file_name, "a") as f:
            writer = csv.writer(f)
            writer.writerow([topic_choice, total_points, username])
        
        total_points = float(total_points)
        # Check to see if new High Score
        #file_name = "list.csv"

        with open(file_name, "r") as f:
            reader = csv.reader(f)
            # reader.__next__()

            music_highscores = []
            history_highscores = []
            cities_highscores = []
            cs_highscores = []
            gk_highscores = []
            
            # Topic number is a list because reading from CSV file
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
            
            # Sorting and reversing the new lists so the highest 
            # numbers are at the start
            music_highscores.sort(reverse=True)
            history_highscores.sort(reverse=True)   
            cities_highscores.sort(reverse=True)
            cs_highscores.sort(reverse=True)
            gk_highscores.sort(reverse=True)
            
            # Make the topic choice and integar
            topic_choice = int(topic_choice)
            
            # If the new total points score is higher than the first
            # score in the new topic list then display new high score
            if topic_choice == 1 and total_points >= music_highscores[0]:
                print(f"[bold purple]New High Score![/bold purple]\n")
                print(f"Conratulations {username} your new Music Quiz Highest Score is [bold red]{total_points:.2f}[/bold red]!\n")
            elif topic_choice == 2 and total_points >= history_highscores[0]:
                print(f"[bold purple]New High Score![/bold purple]\n")
                print(f"Conratulations {username} your new History Quiz Highest Score is [bold red]{total_points:.2f}[/bold red]!\n")
            elif topic_choice == 3 and total_points >= cities_highscores[0]:
                print(f"[bold purple]New High Score![/bold purple]\n")
                print(f"Conratulations {username} your new Capital Cities Quiz Highest Score is [bold red]{total_points:.2f}[/bold red]!\n")
            elif topic_choice == 4 and total_points >= cs_highscores[0]:
                print(f"[bold purple]New High Score![/bold purple]\n")
                print(f"Conratulations {username} your new Computer Science Quiz Highest Score is [bold red]{total_points:.2f}[/bold red]!\n")
            elif topic_choice == 5 and total_points >= gk_highscores[0]:
                print(f"[bold purple]New High Score![/bold purple]\n")
                print(f"Conratulations {username} your new General Knowledge Quiz Highest Score is [bold red]{total_points:.2f}[/bold red]!\n")
        
        # Input staller so user can view information before returning 
        input("\nPress any key for main menu: \n") 
        return 
    
    except: 
        # Unexpected Error Handling
        print("Oops! Something seems to be not working, please try again.")