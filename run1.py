import random

class Board:
    """
    This is the main class. This sets the structure of the game and includes
    methods for actually playing the game.
    """
    def __init__(self):
        self.hit = []
        self.miss = []
        self.ships_found = 0
        self.boats = self.generate_random_ships()

    def generate_random_ships(self):
        boats = []
        while len(boats) <:3
            new_boat = random.randint(0,48)
            if new_boat not in boats:
                boats.append(new_boat)
        return boats

    def get_shots(self):
        while True:
            try:
                row = int(input("\nPick a row (0-4):")) 
                if row < 0 or row > 4:
                    print("Incorrect coordinates. You have to pick a row between 0 and 4.")
                    continue
                col = int(input("Pick a column (0-4):"))  
                if col < 0 or col > 4:
                    print("Incorrect coordinates. You have to pick a column between 0 and 4.")
                    continue

                shot = 5 * row + col  

                else:
                    return shot
            except ValueError:
                print("Incorrect entry, Please enter your number.")

    def check_shot(self, shot):
        if shot in self.boats:
            self.boats.remove(shot)
            self.hit.append(shot)
            self.ships_found += 1
            print (f"That was a HIT! Total ships found: {self.ships_found}\n")
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
        player_name = input("Enter your username: ")
        print("\n")
        print(f"WELCOME {player_name}! Are you ready for a game of Battleship?")
        print("\n")

        print("You have a total of 10 turns to sink 3 hidden ships.")
        print("Guess a row and a column between 0 and 4.")
        print("If you HIT a ship you will see X, if you miss a ship you will see 0.")
        print("If you want to quit the game, type 'exit'.")
        print("GOOD LUCK!")
        print("\n")

        turns_remaining = 10

        for i in range(turns_remaining):
            


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
    

size = 5
num_ships = 3
player_board = Board(size, num_ships, "player")
computer_board = Board(size, num_ships, "computer")


player_board.welcome()
player_board.ship_position()
computer_board.ship_position()

player_board.display_board([], [], show_ships = True)
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