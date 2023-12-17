from random import randint

scores = {"computer": 0, "player": 0}

class Board:
    """
    This is the main class. This sets the structure of the game and includes
    methods for actually playing the game.
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["0" for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def ship_position(self):
        for _ in range(self.num_ships):
            while True:
                ship_row = randint (0, self.size -1)
                ship_col = randint (0, self.size -1)
                if self.board[ship_row][ship_col] == "0":
                    self.ships.append((ship_row, ship_col))
                    break
    
    def player_move(self,guesses):
        while True: 
            try:
                row = input("Pick a row (0-4):")
                if row < 0 or row > 4:
                    print("Incorrect coordinates. You have to pick a row between 0 and 4.")
                    continue
                col = input("Pick a column (0-4):")
                if col < 0 or col > 4:
                    print("Incorrect coordinates. You have to pick a column between 0 and 4.")
                    continue

                shot = 7 * row + col

                if shot in guesses:
                    print("You have already tried this coordinate. Please try another one.")
                else:
                    return shot
            except ValueError:
                print("Please pick a valid number.")

for row in player_board.board:
        print(" ".join(row))

player_move = player_board.get_player_move(player_board.guesses)
player_board.guesses.append(player_move) 
