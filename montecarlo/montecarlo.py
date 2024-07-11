import numpy as np
import pandas as pd
import random

class Die:
    """An object with faces and weights that can be rolled to get results and be used in a game"""
    
    def __init__(self, faces):
        """Initializes Die object with distinct faces from input 
        with a weight of 1.0"""
        if not isinstance(faces, np.ndarray):
            raise TypeError("Please input a numpy array of faces.")
            
        if not len(faces) == len(np.unique(faces)):
            raise ValueError("Faces must be distinct.")  
            
        self.__df = pd.DataFrame.from_dict({face:1.0 for face in faces}, 
                                           orient='index', columns=["Weight"])
        self.__df.index.name = 'Face'
        
        
    def change_weight(self, face, new_weight):
        """Changes the weight of a face of the die.
        Face and new weight specified in arguments."""
        if face not in self.__df.index:
            raise IndexError('Please input a valid face.')
        try:
            float(new_weight)
        except ValueError:
            raise TypeError("Please input a valid weight") from None
        self.__df.loc[face] = float(new_weight)
        
        
    def roll(self, rolls=1):
        """Rolls the die a given amount of times (default 1)
        Returns a list of the outcomes"""
        sample = random.choices(self.__df.index, weights=self.__df["Weight"], k=rolls)
        return(sample)
        
        
    def current_state(self):
        """Returns a copy of the die data frame storing the faces and weights,"""
        return(self.__df)
    
               
class Game:
    """An object that allows you to roll one or more 
    similar Die objects and get the results"""
    
    def __init__(self, dice):
        """Initializes Game object with a list of Die objects"""
        self.dice = dice
        self.__play_df = pd.DataFrame()
        
    def play(self, rolls):
        """Takes an arguement that specifies how many times to roll 
        each die in the list and stores the results in a dataframe"""
        df = pd.DataFrame()
        x = 0
        for die in self.dice:
            df[x] = die.roll(rolls)
            x+=1
        df.index = df.index + 1
        self.__play_df = df
        
    def recent_play(self, form = 'wide'):
        """Shows the results of the most recent play in either a 
        narrow or wide format."""
        if form == 'wide':
            return(self.__play_df)
        elif form == 'narrow':
            return(self.__play_df.stack())
        else:
            raise ValueError("Please only specify narrow or wide format")
        
class Analyzer:
    '''Takes the results of a game and computes 
    descriptive statistics about it'''
    
    def __init__(self, game):
        """Initializes an Analyzer object which takes a Game object
        as an arguement"""
        if isinstance(game, Game):
            self.game = game
        else:
            raise ValueError("Please pass a Game object")
            
    def jackpot(self):
        """Counts how many times a roll in the game resulted in a jackpot
        and returns that number"""
        df = self.game.recent_play()
        uniques = [len(df.loc[row].unique()) for row in df.index]
        x = [1 if u==1 else 0 for u in uniques]
        return sum(x)
        
    def face_counts_per_roll(self):
        """Counts how many times each face is rolled in an event
        and returns a data frame of those results"""
        df = self.game.recent_play()
        values = [df[col].value_counts() for col in df.columns]

        return values
        
    def combo_count(self):
        """Counts the number of distinct combinations of faces rolled
        and returns a data frame of the results"""
        pass
        
    def permutation_count(self):
        """Counts the number of distinct permutations of faces rolled
        and returns a data frame of the results"""
        pass
        