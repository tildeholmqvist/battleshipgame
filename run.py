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
