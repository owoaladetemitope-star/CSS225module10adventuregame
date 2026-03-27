# Chapter 4
# The player reaches an old tower

def play():

    print("Chapter 4: The Old Tower")
    print("You see an old tower. It looks empty, but it could be dangerous.")

    while True:

        print()
        print("What do you want to do?")
        print("1. Enter the tower")
        print("2. Walk around the tower")
        print("3. Go back to the river")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            print("You enter the tower and walk carefully.")
            return "chapter5"

        elif choice == "2":
            print("You walk around the tower and find a small trail forward.")
            return "chapter5"

        elif choice == "3":
            print("You go back to the river.")
            return "chapter3"

        else:
            print("Invalid choice. Please try again.")
