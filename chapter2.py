# Chapter 2
# The player reaches the forest

def play():

    print("Chapter 2: Forest Edge")
    print("You arrive at the edge of a dark forest.")

    while True:

        print()
        print("What do you want to do?")
        print("1. Walk deeper into the forest")
        print("2. Help a traveler on the road")
        print("3. Go back to the village")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            print("You walk deeper into the forest.")
            return "chapter3"

        elif choice == "2":
            print("You help the traveler. They thank you for your kindness.")
            print("The traveler tells you about a river ahead.")
            return "chapter3"

        elif choice == "3":
            print("You return to the village.")
            return "chapter1"

        else:
            print("Invalid choice. Please try again.")
