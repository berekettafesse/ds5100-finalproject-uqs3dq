import numpy as np
import pandas as pd

class Die:
    
    def __init__(self, faces):
        if not isinstance(faces, np.ndarray):
            raise TypeError("Please input a numpy array of faces.")
            
        if not len(faces) == len(np.unique(faces)):
            raise ValueError("Faces must be distinct.")  
            
        self.__df = pd.DataFrame.from_dict({face:1.0 for face in faces}, orient='index', columns=["Weight"])
        print(self.__df)
        
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
        