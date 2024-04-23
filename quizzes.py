import time
from colorama import Fore, Style

def pop():
    start_time = time.time()

    questions = (("\nWhat name is NOT on of Kim or Kanye's children?: \n"), 
                 ("\nWhich popstar is the godmother of both of Elton Johns sons?: \n"), 
                 ("\nWhat is Rihanna's real name?: \n"), 
                 ("\nWhich pop star accidentally set fire to her home gym with candles?: \n"),
                 ("\nWhich pop star was Judge Judy's neighbor?: \n"),
                 
                 )

    options = (("A. Chicago", "B. East", "C. Palm", "D. North"),
               ("A. Mariah Carey", "B. Tina Turner", "C. Lady Gaga", "D. Madonna"),
               ("A. Rihanna Felty", "B. Robyn Fenty", "C. Robin Dern", "D. Rachel Feaner"),
               ("A. Lady Gaga", "B. Rhianna", "C. Miley Cyrus", "D. Britney Spears"),
               ("A. Justin Bieber", "B. Adele", "C. Taylor Swift", "D. Bruno Mars"),
               

    )

    answers = ("B", "C", "B", "D", "A")
    score = 0
    guesses = []
    question_num = 0
    for question in questions:
        print(Fore.BLUE + "-----------------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input(Style.RESET_ALL + "\nEnter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print(Fore.GREEN + "Correct!")
        else: 
            print(Fore.RED + "Incorrect!")
            print(f"{answers[question_num]} is the correct answer.")
        question_num += 1

    end_time = time.time()
    total_time = end_time - start_time

    print(Fore.BLUE + "-----------------------------")
    print("          RESULTS            ")
    print("-----------------------------")
    print()
    print("Answers: ", end=" ")
    for answer in answers:
        print(answer, end = " ")
    print()

    print("Guesses: ", end = " ")
    for guess in guesses:
        print(guess, end = " ")
    print()

    score = int(score / len(questions) * 100)
    print(f"\nYour score is {score}%\n")
    print(f"Total time taken: {total_time: .2f} seconds.")

    points = int(score * 9) - total_time
    print(f"Total points: {points}\n")

def seventies():
    print("70s quiz")
    

def eighties():
    print("80s quiz")
    

def nineties_hiphop():
    print("90s HH")
    

def rocknroll():
    print("rnr quiz")
    