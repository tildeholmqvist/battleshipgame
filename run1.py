import random

class Board:
    def __init__(self):
        self.hit = []
        self.miss = []
        self.ships_found = 0
        self.boats = self.generate_random_ships()

    def generate_random_ships(self):
        boats = []
        while len(boats) < 3:
            new_boat = random.randint(0, 24)
            if new_boat not in boats:
                boats.append(new_boat)
        return boats

    def get_shots(self):
        while True:
            try:
                row = int(input("\nPick a row (0-4): "))
                if row < 0 or row > 4:
                    print("Incorrect coordinates. You have to pick a row between 0 and 4.")
                    continue
                col = int(input("Pick a column (0-4): "))
                if col < 0 or col > 4:
                    print("Incorrect coordinates. You have to pick a column between 0 and 4.")
                    continue

                shot = 5 * row + col
                return shot
            except ValueError:
                print("Incorrect entry. Please enter your number.")

    def check_shot(self, shot):
        if shot in self.boats:
            self.boats.remove(shot)
            self.hit.append(shot)
            self.ships_found += 1
            print(f"That was a HIT! Total ships found: {self.ships_found}\n")
            return True
        else:
            self.miss.append(shot)
            return False

    def display_board(self):
        print(f"\n THE BATTLEFIELD \n")
        print("    0  1  2  3  4 ")
        place = 0
        for x in range(5):
            row = ""
            for y in range(5):
                if place in self.hit:
                    ch = " X "
                elif place in self.miss:
                    ch = " O "
                else:
                    ch = " * "
                row += ch
                place += 1
            print(x, "", row)

    def play_game(self):
        player_name = input("\nHello There! Please enter your username: ")
        print("\n")
        print(f"WELCOME {player_name}! Are you ready for a game of Battleship?")
        print("\n")

        print("You have a total of 10 turns to sink 3 hidden ships.")
        print("Guess a row and a column between 0 and 4.")
        print("If you HIT a ship you will see X, if you miss a ship you will see O.")
        print("If you want to quit the game, type 'exit'.")
        print("\n")
        print("GOOD LUCK!")
        print("\n")

        turns_remaining = 10

        for i in range(turns_remaining):
            print(f"Turns left: {turns_remaining - i}")
            self.display_board()
            shot = self.get_shots()

            try:
                if shot == "exit":
                    user_input = input("Do you want to exit the game? (YES or NO) \n")
                    if user_input.upper() == "YES":
                        return
                elif shot < 0 or shot > 24:
                    print("Incorrect coordinates. You have to pick a number between 0 and 4.")
                else:
                    shot_result = self.check_shot(shot)
                    if shot_result and self.ships_found == 3:
                        print("YOU WIN! Congratulations, you sank all ships!")
                        user_input = input("Do you want to exit the game? (YES or NO) \n")
                        if user_input.upper() == "YES":
                            return
            except ValueError:
                print("Incorrect coordinates. Please enter your guess as a number.\n")

        if len(self.boats) > 0:
            print("GAME OVER! The computer sank all your ships...")

board = Board()
board.play_game()