from apg import assist_leader
from bpg import block_leader
from ppg import scoring_leader
from spg import steal_leader
from rbpg import rebounding_leader


class Scraper:
    def __init__(self, scoring, blocks, assists, rebounding, steals):
        self.scoring = scoring
        self.blocks = blocks
        self.assists = assists
        self.rebounding = rebounding
        self.steals = steals
        
    def points_per_game(self):
        return
    
    def blocks_per_game(self):
        return
    
    def assists_per_game(self):
        return
    
    def steals_per_game(self):
        return
    
    def rebounds_per_game(self):
        return   