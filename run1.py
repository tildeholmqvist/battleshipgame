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
            username = input("Please enter your name to begin the game.\n")

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

    def display_board(self, hit, miss):
        print("    THE BATTLEFIELD    ")
        print("    0  1  2  3  4 ")
        place = 0
        for x in range(5):
            row = ""
            for y in range(5):
                if place in hit:
                    ch = " X "
                elif place in miss:
                    ch = " O "
                else:
                    ch = " * "
                row += ch
                place += 1
            print(x, "", row)
    
    def get_player_shot(self, guesses, computer_board):
        while True:
            try:
                row = int(input("Pick a row (0-4):"))  # Convert input to int
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
                        print("That was a HIT!")
                        computer_board.ships.remove(shot)
                        guesses.append(shot)
                        return True
                    else:
                        print("That was a MISS!")
                        guesses.append(shot)
                        return False
            except ValueError:
                print("Please pick a valid number.")




size = 5
num_ships = 3
player_board = Board(size, num_ships, "player")
computer_board = Board(size, num_ships, "computer")


player_board.welcome()
player_board.ship_position()

guesses = [] 
player_shot_result = player_board.get_player_shot(guesses, computer_board)

if player_shot_result:
    player_board.display_board([], [player_shot_result]) 
else:
    player_board.display_board([], [player_shot_result])

player_board.display_board([0, 1, 2], [3, 4, 5])
