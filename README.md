# Monte Carlo Simulator
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




