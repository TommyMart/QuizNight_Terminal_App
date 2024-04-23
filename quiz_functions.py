from quizzes import pop, seventies, eighties, nineties_hiphop, rocknroll


def quiz_topics():
    print("\nQUIZ TOPICS\n")
    print("1. Pop Culture")
    print("2. 70's Classics")
    print("3. 80's Classics")
    print("4. 90's Hip Hop")
    print("5. Rock n Roll")
    print("6. Back to main menu")

    topic_choice = input("\nPlease enter your selection: \n")
    

    if topic_choice == "1":
        pop()
    elif topic_choice == "2":
        seventies()
    elif topic_choice == "3":
        eighties()
    elif topic_choice == "4":
        nineties_hiphop()
    elif topic_choice == "5":
        rocknroll()
    elif topic_choice == "6":
        return 
    else: 
        print("Please only input corresponding topic numbers shown above.")
        quiz_topics()
            
def top_scores():
    print("top")

def random_quiz():
    print("random")

def create_new():
    print("new")

