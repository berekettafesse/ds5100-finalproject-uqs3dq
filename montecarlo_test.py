import unittest
import pandas as pd
import numpy as np
from montecarlo import montecarlo

class MontecarloTestSuite(unittest.TestCase):
    
    def test_1_die_init(self):
        """TypeError is raised when not a numpy array"""
        with self.assertRaises(TypeError):
            die = montecarlo.Die([1,2,3,4,5,6])
    
    def test_2_die_init(self):
        """ValueError is raised when not distinct face values"""
        with self.assertRaises(ValueError):
            die = montecarlo.Die(np.array([1,1,2,3,4,5]))
            
    def test_3_current_state(self):
        """After Die initialization only contains weights of 1.0"""
        die = montecarlo.Die(np.array([1,2,3,4,5,6]))
        assert all(x == 1.0 for x in die.current_state()['Weight'])
        
    def test_4_change_weight(self):
        """Change weight method works correctly"""
        die = montecarlo.Die(np.array([1,2,3,4,5,6]))
        die.change_weight(3, 0.01)
        assert die.current_state().loc[3,'Weight'] == 0.01
        
    def test_5_change_weight(self):
        """TypeError is raised when an invalid weight in input 
        into change_weight"""
        with self.assertRaises(TypeError):
            die = montecarlo.Die(np.array([1,2,3,4,5,6]))
            die.change_weight(3, 'not a number')        
    def test_6_change_weight(self):
        """IndexError is raised when an invalid face is input 
        into change_weight"""
        with self.assertRaises(IndexError):
            die = montecarlo.Die(np.array([1,2,3,4,5,6]))
            die.change_weight('not a face', 0)    
            
    def test_7_roll(self):
        """Rolls appropriate amount of times"""
        die = montecarlo.Die(np.array([1,2,3,4,5,6]))
        assert len(die.roll(12)) == 12

    def test_8_current_state(self):
        """Current state is a pandas df"""
        die = montecarlo.Die(np.array([1,2,3,4,5,6]))
        assert isinstance(die.current_state(), pd.DataFrame)
        
    def test_9_game_init(self):
        """Game dice are Die objects"""
        a = montecarlo.Die(np.array([1,2,3,4,5,6]))
        b = montecarlo.Die(np.array([1,2,3,4,5,6]))
        c = montecarlo.Die(np.array([1,2,3,4,5,6]))
        d = montecarlo.Die(np.array([1,2,3,4,5,6]))
        game = montecarlo.Game([a,b,c,d])

        assert all(isinstance(x, montecarlo.Die) for x in game.dice)
        
    def test_10_play(self):
        """Play result has proper dimensions"""
        a = montecarlo.Die(np.array([1,2,3,4,5,6]))
        b = montecarlo.Die(np.array([1,2,3,4,5,6]))
        c = montecarlo.Die(np.array([1,2,3,4,5,6]))
        d = montecarlo.Die(np.array([1,2,3,4,5,6]))
        game = montecarlo.Game([a,b,c,d])
        
        game.play(3)
        played = game.recent_play()
        assert ((len(played.columns) == len(game.dice)) and (len(played.index) == 3))
        
    def test_11_recent_play(self):
        """Narrow argument returns narrow table"""
        a = montecarlo.Die(np.array([1,2,3,4,5,6]))
        b = montecarlo.Die(np.array([1,2,3,4,5,6]))
        c = montecarlo.Die(np.array([1,2,3,4,5,6]))
        d = montecarlo.Die(np.array([1,2,3,4,5,6]))
        game = montecarlo.Game([a,b,c,d])
        
        game.play(3)
        played = game.recent_play("narrow")   
        assert len(played.columns) == 1
        
    def test_11_recent_play(self):
        """Invalid argument raises ValueError"""
        with self.assertRaises(ValueError):
            a = montecarlo.Die(np.array([1,2,3,4,5,6]))
            b = montecarlo.Die(np.array([1,2,3,4,5,6]))
            c = montecarlo.Die(np.array([1,2,3,4,5,6]))
            d = montecarlo.Die(np.array([1,2,3,4,5,6]))
            game = montecarlo.Game([a,b,c,d])

            game.play(3)
            played = game.recent_play("not an arg")     
            
    def test_12_analyzer_init(self):
        """Raises ValueError if game object not passed"""
        with self.assertRaises(ValueError):
            a = montecarlo.Analyzer("not a game")
            
            
    
if __name__ == '__main__':
    
    unittest.main(verbosity=3)  