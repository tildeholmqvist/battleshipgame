import random

class BattleshipGame:
    def __init__(self):
        self.hit = []
        self.miss = []
        self.ships_found = 0
        self.player_name = ""
    
    def get_shot(shot):
        