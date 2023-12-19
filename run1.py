import random

class BattleshipGame:
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
            shot = 7 * row + col

            if shot < 0 or shot > 48:
                print("Incorrect coordinates, Please try again")
            elif shot in guesses:
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
    
    def display_board(self, hits, misses):
        

