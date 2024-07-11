## Metadata
Project: Monte Carlo Simulator
Author: Bereket Tafesse

## Synopsis
### How to use:
#### Installation:
- Open a terminal
- cd to the directory on your device in which you can clone the repository with the package
- Run:
    - git clone https://github.com/berekettafesse/ds5100-finalproject-uqs3dq.git
    - cd finalproject-uqs3dq
    - pip install -e .

#### Importing
- In a python file or shell you can run:
    - import montecarlo.montecarlo
- From this, to access the classes, run:
    - from montecarlo.montecarlo import Die, Game, Analysis
    
#### Usage
- To create a Die:
```python
## np.ndarray input with faces of the die
die = Die(np.array([1,2,3,4,5,6]))
## Using current_state method for example
die.current_state()
```
- To play a Game:
```python
## list of Die objects as input
game = Game([die, die, die])
## Using roll method for example
game.roll(10)
```
- To analyze a Game
```python
## played Game object as input
analyzer = Analyzer(game)
## Using Jackpot method for example
analyzer.jackpot()
```

## API Description 
To see this information in python file or shell, run:
```python
help(montecarlo.montecarlo)
```

    class Analyzer(game)
     |  
     |  Takes the results of a game and computes 
     |  descriptive statistics about it
     |  
     |  Attributes:
     |    game: a played Game object
     |  
     |  Methods:
     |  __init__(self, game)
     |      Initializes an Analyzer
     |      
     |      Parameters:
     |      game (Game): A game object that has been played
     |  
     |  combo_count(self)
     |      Counts the number of distinct combinations of faces rolled
     |      
     |      Returns:
     |      pd.DataFrame: table with an index of the combination of faces and value of frequency
     |  
     |  face_counts_per_roll(self)
     |      Counts how many times each face is rolled
     |      
     |      Returns:
     |      pd.DataFrame: number of times a face was rolled in each event
     |  
     |  jackpot(self)
     |      Counts how many times a roll resulted in a jackpot
     |      
     |      Returns:
     |      int: number of jackpots
     |  
     |  permutation_count(self)
     |      Counts the number of distinct permutations of faces rolled
     |      
     |      Returns:
     |      pd.DataFrame: table with an index of the permutation of faces and value of frequency
    
    class Die(faces)
     |  
     |  An object with faces and weights that can be rolled to get results and be used in a game
     | 
     |  Methods:
     |  
     |  __init__(self, faces)
     |      Initializes Die object to have weight = 1.0 for all faces.
     |      
     |      Parameters: 
     |      faces (np.ndarray): An array of faces for the die that can be strings or numbers
     |  
     |  change_weight(self, face, new_weight)
     |      Changes the weight of a face of the die.
     |      
     |      Parameters:  
     |      face (str,int): The face of the die to be changed
     |      new_weight: The new weight of the specified face
     |  
     |  current_state(self)
     |      Returns:
     |      pd.DataFrame: copy of the die data frame storing the faces and weights
     |  
     |  roll(self, rolls=1)
     |      Rolls the die a given amount of times
     |      
     |      Parameters:
     |      rolls (int): How many times to roll the die. Default = 1
     |      
     |      Returns:
     |      list: outcomes

    class Game(dice)
     |  
     |  An object that allows you to roll one or more similar Die objects and get the results
     |  
     |  Attributes:
     |    dice: a list of similarly faced Die objects to play the game with
     | 
     |  Methods defined here:
     |  
     |  __init__(self, dice)
     |      Initializes Game object
     |      
     |      Parameters: 
     |      dice ([Die]): a list of Die objects with the same faces
     |  
     |  play(self, rolls)
     |      Rolls each die and stores the results in a dataframe
     |      
     |      Parameters:
     |      rolls (int): how many times to roll each die
     |  
     |  recent_play(self, form='wide')
     |      Shows the results of the most recent play
     |      
     |      Parameters:
     |      form (str): how to format the results, wide/narrow. Default wide
