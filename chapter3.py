# Chapter 3
# The player reaches a river

def play():

    print("Chapter 3: The River")
    print("You arrive at a wide river blocking your path.")

    while True:

        print()
        print("What do you want to do?")
        print("1. Try to cross the river")
        print("2. Walk along the river")
        print("3. Go back to the forest")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            print("You carefully cross the river.")
            return "chapter4"

        elif choice == "2":
            print("You walk along the river and find a path.")
            return "chapter4"

        elif choice == "3":
            print("You return to the forest.")
            return "chapter2"

        else:
            print("Invalid choice. Please try again.")
