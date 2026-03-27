# Chapter 1
# This chapter starts the game in the village

def play():

    print("Chapter 1: The Village Edge")
    print("You wake up near a small village.")

    while True:

        print()
        print("What do you want to do")
        print("1. Walk north")
        print("2. Enter the village")
        print("3. Wait")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            print("You walk north toward the forest.")
            return "chapter2"

        elif choice == "2":
            print("You walk into the village and look around.")
            print("People warn you that the forest ahead is dangerous.")
            return "chapter2"

        elif choice == "3":
            print("You wait for a while. Nothing happens.")

        else:
            print("Invalid choice. Please try again.")
