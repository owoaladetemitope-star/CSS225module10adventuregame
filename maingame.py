import chapter1
import chapter2
import chapter3
import chapter4
import chapter5

class Game:
    def __init__(self):
        self.current = "chapter1"

    def run(self):
        while True:

            if self.current == "chapter1":
                self.current = chapter1.play()

            elif self.current == "chapter2":
                self.current = chapter2.play()

            elif self.current == "chapter3":
                self.current = chapter3.play()

            elif self.current == "chapter4":
                self.current = chapter4.play()

            elif self.current == "chapter5":
                self.current = chapter5.play()

            elif self.current == "win":
                print()
                print("You win. Thanks for playing.")
                break

            elif self.current == "lose":
                print()
                print("Game over. Thanks for playing.")
                break

            else:
                print()
                print("Error: Unknown chapter name:", self.current)
                break


if __name__ == "__main__":
    game = Game()
    game.run()
