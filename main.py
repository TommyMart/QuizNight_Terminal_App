


print("\nHello, and welcome to Tom's Music Quiz!\n")

def menu():
    print("1. Enter 1 for quiz topics")
    print("2. Enter 2 for top scores")
    print("3. Enter 3 to start a random quiz")
    print("4. Enter 4 to create a new text quiz")
    print("5. Enter 5 to exit quiz")

    user_choice = input("\nPlease enter your selection: \n")
    return user_choice

print(menu())
