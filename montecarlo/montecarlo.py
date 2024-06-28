import numpy as np

class Die:
    
    def __init__(self):
        # try:
        #     isinstance(faces, np.ndarray)
        # except:
        #     raise TypeError("Please input a numpy array of faces.")
        # try:
        #     len(faces) == len(faces.unique())
        # except:
        #     raise ValueError("Please input an array of distinct values.")  
        pass
        
    def change_weight(self):
        pass
        
    def roll(self):
        pass
        
    def current_state(self):
        pass
               
class Game:
    
    def __init__(self):
        pass
        
    def play(self):
        pass
        
    def recent_play(self):
        pass
        
class Analyzer:
    '''Takes the results of a game and computes 
    descriptive statistics about it'''
    
    def __init__(self, game):
        try:
            isinstance(game, Game)
        except:
            raise ValueError("Please input a Game.")
            
    def jackpot(self):
        pass
        
    def face_counts_per_roll(self):
        pass
        
    def combo_count(self):
        pass
        
    def permutation_count(self):
        pass
        