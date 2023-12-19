import random

class Board:
    def __init__(self):
        self.player_hit = []
        self.player_miss = []
        self.player_ships_found = 0
        self.player_boats = self.generate_random_ships()

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
                    print(f"Incorrect coordinate. Choose a number between 0 - 4.")
                    continue
                return coordinate
            except ValueError:
                print("Incorrect coordinate. Please pick a valid coordinate.")
    
    def get_shot(self):
        while True:
            row = self.get_coordinate("Row")
            if row == "exit":
                return "exit"

            col = self.get_coordinate("Column")
            shot = 5 * row + col

            if shot < 0 or shot > 25:
                print("Incorrect coordinates, Please try again")
            elif shot in self.player_hit or shot in self.player_miss or shot in self.comp_hit or shot in self.comp_miss:
                print("Incorrect, it's already been used.")
            else:
                return shot
    
    def check_shot(self, shot, boats, hit, miss):
        if shot in boats:
            boats.remove(shot)
            hit.append(shot)
            return True
        else:
            miss.append(shot)
            return False
    
    def display_board(self, hits, misses, player_board=False):
        print("·· BATTLESHIP BOARD ··")
        print("\n    0  1  2  3  4")
        place = 0
        for x in range(5):
            row = ""
            for y in range(5):
                place = 5 * x + y
                if place in hits:
                    ch = " X "
                elif place in misses:
                    ch = " * "
                elif player_board and place in self.player_boats:
                    ch = " @ "
                else:
                    ch = " · "
                row += ch
                place += 1
            print(x, "", row)
    
    def comp_turn(self):
        guess = random.randint(0, 24)
        return guess
    
    def play_game(self):
        player_hit = self.player_hit
        player_miss = self.player_miss
        player_ships_found = self.player_ships_found
        player_boats = self.player_boats

        comp_hit = self.comp_hit
        comp_miss = self.comp_miss
        comp_ships_found = self.comp_ships_found
        comp_boats = self.comp_boats

        player_name = input("\nHello There! Please enter your username: ")
        print(f"\nWELCOME {player_name}! Are you ready for a game of Battleship?")
        print("\nYou have a total of 20 turns to sink 3 hidden ships.")
        print("Guess a row and a column between 0 and 4.")
        print("If you HIT a ship, you will see 'X'.")
        print("If you miss a ship, you will see '*'.")
        print("\nIf you want to quit the game, type 'exit'.\nGOOD LUCK!\n")

        turns_remaining = 20

        for i in range(turns_remaining):
            print(f"Turns left: {turns_remaining - i}")
            self.display_board(player_hit, player_miss)
            self.display_board(comp_hit, comp_miss, player_board=True)
        
            guesses = player_hit + player_miss
            shot = self.get_shot()
            print("\n")

            if shot == "exit":
                    user_input = input("Do you want to exit the game? (YES or NO) \n")
                    if user_input.upper() == "YES":
                        print("Exiting the game...")
                        return
            try:
                shot = int(shot)
                if shot < 0 or shot > 24:
                    print("Incorrect coordinates. You have to pick a number between 0 and 4.")
                elif shot in guesses:
                    print("You already tried this coordinate. Try again.")
                else:
                    player_result = self.check_shot(shot, comp_boats, player_hit, player_miss)
                    if player_result and comp_ships_found == 3:
                        print("YOU WIN! Congratulations, you sank all ships!")
                        user_input = input("Do you want to exit the game? (YES or NO) \n") 
                        if user_input.upper() == "YES":
                            return
                
                comp_shot = self.comp_turn()
                comp_result = self.check_shot(comp_shot, player_boats, comp_hit, comp_miss)
                if comp_result and player_ships_found == 3:
                    print("GAME OVER! The computer sank all your ships...")
                    return
                
            except ValueError:
                    print("Incorrect coordinates. Please enter your guess as a number.\n")
                    print("\n")
                
        if len(player_boats) > 0:
            print("GAME OVER! Better luck next time...")

board = Board()
board.play_game()