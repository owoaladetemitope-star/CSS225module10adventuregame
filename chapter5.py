# Chapter 5
# The final chapter with endings

def play():

    print("Chapter 5: The Gate")
    print("You reach a gate at the edge of the land.")

    while True:

        print()
        print("What do you want to do?")
        print("1. Go through the gate (escape)")
        print("2. Stay and rest (you might lose time)")
        print("3. Go back to the tower")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            print("You go through the gate and escape safely.")
            return "win"

        elif choice == "2":
            print("You rest too long. Danger catches up to you.")
            return "lose"

        elif choice == "3":
            print("You go back to the tower.")
            return "chapter4"

        else:
            print("Invalid choice. Please try again.")
