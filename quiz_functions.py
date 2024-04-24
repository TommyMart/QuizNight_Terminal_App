from quizzes import quiz
import random
from colorama import Fore, Style, Back

def quiz_topics(rand_quiz=None):
    print("\nQUIZ TOPICS\n")
    print("1. Pop Culture")
    print("2. 70's Classics")
    print("3. 80's Classics")
    print("4. 90's Hip Hop")
    print("5. Rock n Roll")
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
        quiz(questions, options, answers)
        
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
        quiz(questions, options, answers)

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
        quiz(questions, options, answers)

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
        quiz(questions, options, answers)

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
        quiz(questions, options, answers)

    elif topic_choice == "6":
        return 
    else: 
        print("Please only input corresponding topic numbers shown above.")
        quiz_topics()
            
def top_scores(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)

def random_quiz():
    rand_quiz = random.randint(1, 5)
    quiz_topics(rand_quiz)
    

def create_new():
    print("new")

