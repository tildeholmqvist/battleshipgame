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

    
    def welcome():
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

Board.welcome() 
