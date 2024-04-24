import time
from colorama import Fore, Style, Back   

def calculate_points(score, total_questions, total_time):
    # Score points: 50 points for each correct answer
    score_points = score * 50
    
    # Time points: 1 point for each second saved
    max_time = total_questions * 30  # Assuming 30 seconds per question
    time_points = (max_time - total_time) if total_time < max_time else 0
    
    # Total points: sum of score points and time points
    total_points = score_points + time_points
    
    return total_points

def quiz_function():
    score = 0
    guesses = []
    question_num = 0
    start_time = time.time()
    for question in questions:
        print(Fore.BLUE + Style.BRIGHT + "-----------------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input(Style.RESET_ALL + "\nEnter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print(Fore.GREEN + Style.BRIGHT + "Correct!")
        else: 
            print(Fore.RED + Style.BRIGHT + "Incorrect!")
            print(f"{answers[question_num]} is the correct answer.")
        question_num += 1
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print(Fore.BLUE + Style.BRIGHT + "-----------------------------")
    print("          RESULTS            ")
    print("-----------------------------")
    
    print("Answers: ", end=" ")
    for answer in answers:
        print(answer, end=" ")
    
    print("\nGuesses: ", end=" ")
    for guess in guesses:
        print(guess, end=" ")
    
    score = int(score / len(questions) * 100)
    print(f"\nYour score is {score}%")
    print(f"Total time taken: {total_time:.2f} seconds")

    # Calculate total points based on score and time
    total_points = calculate_points(score, len(questions), total_time)
    print(f"Total points: {total_points}")