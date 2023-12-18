from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    """
    This is the main class. This sets the structure of the game and includes
    methods for actually playing the game.
    """

    def __init__(self, size, num_ships, name):
        self.size = size
        self.board = [["0" for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.guesses = []
        self.ships = []

    def welcome(self):
        """
        Welcome the user by a welcome message and ask them for their username
        """
        print("WELCOME PLAYER!")
        print("Are you ready for a game of Battleship?\n")
        while True:
            username = input("Please enter your name to begin the game: \n")

            if len(username) == 0:
                print("Username must contain letters or numbers.\n")
            else:
                break
        print(f"\nHello {username}, let's start the game!\n")

    def ship_position(self):
        for _ in range(self.num_ships):
            while True:
                ship_row = randint(0, self.size - 1)
                ship_col = randint(0, self.size - 1)
                if self.board[ship_row][ship_col] == "0":
                    self.ships.append((ship_row, ship_col))
                    break
    
    def player_shot(self, guesses, computer_board):
        while True:
            try:
                row = int(input("\nPick a row (0-4):"))  # Convert input to int
                if row < 0 or row > 4:
                    print("Incorrect coordinates. You have to pick a row between 0 and 4.")
                    continue
                col = int(input("Pick a column (0-4):"))  # Convert input to int
                if col < 0 or col > 4:
                    print("Incorrect coordinates. You have to pick a column between 0 and 4.")
                    continue

                shot = 5 * row + col  

                if shot in guesses:
                    print("You have already tried this coordinate. Please try another one.")
                else:
                    if shot in computer_board.ships:
                        print("\nThat was a HIT!\n")
                        computer_board.ships.remove(shot)
                        guesses.append(shot)
                        return True
                    else:
                        print("\nThat was a MISS!\n")
                        guesses.append(shot)
                        return False
            except ValueError:
                print("Please pick a valid number.")
    
    def computer_shot(self, guesses, player_board):
        while True:
            comp_row = randint(0, self.size -1)
            comp_col = randint(0, self.size -1)
            comp_shot = 5 * comp_row + comp_col

            if comp_shot not in guesses:
                guesses.append(comp_shot)
                if comp_shot in player_board.ships:
                    print("\n The computer HIT your ship!")
                    player_board.ships.remove(comp_shot)
                    return True
                else:
                    print("\n The computer MISSED!")
                    return False
    
    def check_score(self):
        return len(self.ships) == 0
    
    def display_board(self, hit, miss):
        print("\n THE BATTLEFIELD    \n")
        print("    0  1  2  3  4 ")
        place = 0
        for x in range(5):
            row = ""
            for y in range(5):
                if (x, y) in self.ships:
                    ch = " @ "
                elif place in hit:
                    ch = " X "
                elif place in miss:
                    ch = "0"
                else:
                    ch = " * "
                row += ch
                place += 1
            print(x, "", row)

size = 5
num_ships = 3
player_board = Board(size, num_ships, "player")
computer_board = Board(size, num_ships, "computer")


player_board.welcome()
player_board.ship_position()
computer_board.ship_position()

player_board.display_board([], [])
computer_board.display_board([], [])

player_guesses = [] 
computer_guesses = []

while True:
    player_shot_result = player_board.player_shot(player_guesses, computer_board)
    player_board.display_board(player_guesses, computer_guesses)

    if player_board.check_score():
        print("\nYou WIN! Congratulations, you sank all the computers ships!")
        break

    computer_shot_result = computer_board.computer_shot(computer_guesses, player_board)
    player_board.display_board(player_guesses, computer_guesses)

    if computer_board.check_score():
        print("\n You lost... The computer sank all your ships.")
        break