


print("\nHello, and welcome to Tom's Music Quiz!\n")

def menu():
    print("1. Enter 1 for quiz topics")
    print("2. Enter 2 for top scores")
    print("3. Enter 3 to start a random quiz")
    print("4. Enter 4 to create a new text quiz")
    print("5. Enter 5 to exit quiz")

    user_choice = input("\nPlease enter your selection: \n")
    return user_choice

choice = ""

while choice != "5":
    choice = menu()

    if choice == "1":
        print("1")
    elif choice == "2":
        print("2")
    elif choice == "3":
        print("3")
    elif choice == "4":
        print("4")
    elif choice == "5":
        print("5")
    else: 
        print("Please only input options shown above.")
    

print("Thanks for taking the quiz. I hope you enjoyed yourself!")