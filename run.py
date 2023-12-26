import random


class Board:
    def __init__(self):
        self.player_hit = []
        self.player_miss = []
        self.player_ships_found = 0
        self.player_boats = self.generate_random_ships()
        self.player_attempts = set()

        self.comp_hit = []
        self.comp_miss = []
        self.comp_ships_found = 0
        self.comp_boats = self.generate_random_ships()

    def generate_random_ships(self):
        return random.sample(range(25), 3)

    def get_coordinate(self, dimension):
        while True:
            try:
                coordinate = int(input(f"Pick a {dimension} 0 - 4: "))
                if coordinate not in range(5):
                    print("Incorrect coordinate.")
                    print("Choose a number between 0 - 4.")
                    continue
                return coordinate
            except ValueError:
                print(f"Incorrect coordinate.")
                print("Choose a number between 0 - 4.")

    def get_shot(self):
        while True:
            row_input = input("\nPick a Row (0 - 4) or type 'exit' to quit:")
            if row_input.lower() == 'exit':
                return 'exit'

            try:
                row = int(row_input)
                if row not in range(5):
                    print("Incorrect coordinate.")
                    print("Choose a number between 0 - 4.")
                    continue
            except ValueError:
                print("Incorrect input. Please enter a number or type 'exit'.")
                continue

            col_input = input("Pick a Column (0 - 4) or type 'exit' to quit:")
            if col_input.lower() == 'exit':
                return 'exit'

            try:
                col = int(col_input)
                if col not in range(5):
                    print("Incorrect coordinate.")
                    print("Choose a number between 0 - 4.")
                    continue
            except ValueError:
                print("Incorrect input. Please enter a number or type 'exit'.")
                continue

            coordinate = 5 * row + col

            if coordinate in self.player_attempts:
                print("You already tried this coordinate. Try again.")
            else:
                self.player_attempts.add(coordinate)
                return coordinate

    def check_shot(self, shot):
        if shot in self.comp_boats:
            self.comp_boats.remove(shot)
            self.player_hit.append(shot)
            self.player_ships_found += 1
            print("\nThat was a HIT!")
            print(f"Total ships found by you: {self.player_ships_found}\n")
            return True
        else:
            self.player_miss.append(shot)
            print("\nThat was a MISS!")
            print(f"Total ships found by you: {self.player_ships_found}\n")
            return False

    def check_comp_shot(self, shot):
        if shot in self.player_boats:
            self.player_boats.remove(shot)
            self.comp_hit.append(shot)
            self.comp_ships_found += 1
            print("\nThat was a HIT!")
            print(f"Ships found by the computer: {self.comp_ships_found}\n")
            return True
        else:
            self.comp_miss.append(shot)
            print("\nThat was a MISS!")
            print(f"Ships found by the computer: {self.comp_ships_found}\n")
            return False

    def display_player_board(self):
        print(f"\n YOUR BOARD ")
        print("\n    0  1  2  3  4")
        for x in range(5):
            row = ""
            for y in range(5):
                place = 5 * x + y
                if place in self.comp_hit:
                    ch = " X "
                elif place in self.comp_miss:
                    ch = " O "
                elif place in self.player_boats:
                    ch = " @ "
                else:
                    ch = " · "
                row += ch
                place += 1
            print(x, "", row)

    def display_comp_board(self):
        print(f"\n COMPUTER'S BOARD ")
        print("\n    0  1  2  3  4")
        for x in range(5):
            row = ""
            for y in range(5):
                place = 5 * x + y
                if place in self.player_hit:
                    ch = " X "
                elif place in self.player_miss:
                    ch = " O "
                else:
                    ch = " · "
                row += ch
                place += 1
            print(x, "", row)

    def comp_turn(self):
        guess = random.randint(0, 24)
        while guess in self.comp_hit or guess in self.comp_miss:
            guess = random.randint(0, 24)
        return guess

    def play_game(self):
        while True:
            player_name = input("\nHello There! Please enter your username: ")
            if player_name.strip():
                break
            else:
                print("Your username has to include a character.")

        print(f"\nWELCOME {player_name}!")
        print("Are you ready for a game of Battleship?")
        print("\nYou have a total of 20 turns to sink 3 hidden ships.")
        print("Guess a row and a column between 0 and 4.")
        print("If you HIT a ship, you will see 'X'.")
        print("If you MISS a ship, you will see 'O'.")
        print("Your ships is displayed as '@'.")
        print("\nIf you want to quit the game, type 'exit'.\nGOOD LUCK!\n")

        turns_remaining = 20

        for i in range(turns_remaining):
            print(f"Turns left: {turns_remaining - i}")
            self.display_player_board()
            self.display_comp_board()
            shot = self.get_shot()

            if shot == "exit":
                user_input = input("Do you want to exit the game? (YES/NO)\n")
                if user_input.lower() == "yes":
                    print("Exiting the game...")
                    return
                else:
                    turns_remaining += 1
                    continue
            try:
                shot = int(shot)
                if shot < 0 or shot > 24:
                    print("Incorrect coordinate.")
                    print("Choose a number between 0 - 4.")
                    continue

                else:
                    shot_result = self.check_shot(shot)
                    if shot_result and self.player_ships_found > 2:
                        print("YOU WIN! Congratulations, you sank all ships!")
                         self.display_comp_board()
                        return

                comp_shot = self.comp_turn()
                comp_shot_result = self.check_comp_shot(comp_shot)
                if comp_shot_result and self.comp_ships_found > 2:
                    print("GAME OVER! The computer sank all your ships...")
                    self.display_player_board()
                    return

            except ValueError:
                print("Incorrect coordinates.")
                print("Please enter your guess as a number.\n")

        if len(self.comp_boats) > 0:
            print("GAME OVER! Better luck next time...")


if __name__ == "__main__":
    play_again = True
    while play_again:
        board = Board()
        board.play_game()
        user_play = input("Enter 'play' to start over,anything else to quit:")
        play_again = user_play.lower() in ['play']
        if play_again is False:
            print('Thank you for playing, see you soon...')
