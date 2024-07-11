import numpy as np
import pandas as pd
import random

class Die:
    """An object with faces and weights that can be rolled to get results and be used in a game"""
    
    def __init__(self, faces):
        """Initializes Die object to have weight = 1.0 for all faces.
        
        Parameters: 
        faces (np.ndarray): An array of faces for the die that can be strings or numbers
        """
        
        if not isinstance(faces, np.ndarray):
            raise TypeError("Please input a numpy array of faces.")
            
        if not len(faces) == len(np.unique(faces)):
            raise ValueError("Faces must be distinct.")  
            
        self.__df = pd.DataFrame.from_dict({face:1.0 for face in faces}, 
                                           orient='index', columns=["Weight"])
        self.__df.index.name = 'Face'
        
        
    def change_weight(self, face, new_weight):
        """Changes the weight of a face of the die.
        
        Parameters:
        
        face (str,int): The face of the die to be changed
        new_weight: The new weight of the specified face
        """
        if face not in self.__df.index:
            raise IndexError('Please input a valid face.')
        try:
            float(new_weight)
        except ValueError:
            raise TypeError("Please input a valid weight") from None
        self.__df.loc[face] = float(new_weight)
        
        
    def roll(self, rolls=1):
        """Rolls the die a given amount of times
        
        Parameters:
        rolls (int): How many times to roll the die. Default = 1
        
        Returns:
        list: outcomes"""
        sample = random.choices(self.__df.index, weights=self.__df["Weight"], k=rolls)
        return(sample)
        
        
    def current_state(self):
        """
        Returns:
        pd.DataFrame: copy of the die data frame storing the faces and weights"""
        return(self.__df.copy())
    
               
class Game:
    """An object that allows you to roll one or more 
    similar Die objects and get the results"""
    
    def __init__(self, dice):
        """Initializes Game object
        
        Parameters: 
        dice ([Die]): a list of Die objects with the same faces """
        self.dice = dice
        self.__play_df = pd.DataFrame()
        
    def play(self, rolls):
        """Rolls each die and stores the results in a dataframe
        
        Parameters:
        rolls (int): how many times to roll each die"""
        df = pd.DataFrame()
        x = 0
        for die in self.dice:
            df[x] = die.roll(rolls)
            x+=1
        df.index = df.index + 1
        self.__play_df = df
        
    def recent_play(self, form = 'wide'):
        """Shows the results of the most recent play
        
        Parameters:
        form (str): how to format the results, wide/narrow. Default wide"""
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
        """Initializes an Analyzer
        
        Parameters:
        game (Game): A game object that has been played"""
        if isinstance(game, Game):
            self.game = game
        else:
            raise ValueError("Please pass a Game object")
            
    def jackpot(self):
        """Counts how many times a roll resulted in a jackpot
        
        Returns:
        int: number of jackpots
        """
        df = self.game.recent_play()
        uniques = [len(df.loc[row].unique()) for row in df.index]
        x = [1 if u==1 else 0 for u in uniques]
        return sum(x)
        
    def face_counts_per_roll(self):
        """Counts how many times each face is rolled
        
        Returns:
        pd.DataFrame: number of times a face was rolled in each event"""
        df = self.game.recent_play()
        
        new_df = pd.DataFrame(index=self.game.dice[0].current_state().index)
        new_df.index.name = "Roll"
        
        x = 1
        for row in df.index:
            counts = df.loc[row].value_counts()
            new_df[x] = [counts[i] if i in counts.index else 0 for i in new_df.index]
            x+=1

        return new_df.transpose()
        
    def combo_count(self):
        """Counts the number of distinct combinations of faces rolled
        
        Returns:
        pd.DataFrame: table with an index of the combination of faces and value of frequency"""
        df = self.game.recent_play()
        df = df.transpose()
        sorted_df = df.apply(lambda x: 
                             x.sort_values().reset_index(drop = True)).transpose()
        return sorted_df.value_counts().to_frame()
        
    def permutation_count(self):
        """Counts the number of distinct permutations of faces rolled
        
        Returns:
        pd.DataFrame: table with an index of the permutation of faces and value of frequency"""
        df = self.game.recent_play()
        return df.value_counts().to_frame()
        