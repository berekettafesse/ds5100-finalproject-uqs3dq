import unittest
import pandas as pd
import numpy as np
from montecarlo import montecarlo

class MontecarloTestSuite(unittest.TestCase):
    
    def test_1_die_init(self):
        with self.assertRaises(TypeError):
            die = montecarlo.Die([1,2,3,4,5,6])
    
    def test_2_die_init(self):
        with self.assertRaises(ValueError):
            die = montecarlo.Die(np.array([1,1,2,3,4,5]))
            
    def test_3_current_state(self):
        die = montecarlo.Die(np.array([1,2,3,4,5,6]))
        assert all(x == 1.0 for x in die.current_state()['Weight'])
        
    def test_4_change_weight(self):
        die = montecarlo.Die(np.array([1,2,3,4,5,6]))
        die.change_weight(3, 0.01)
        assert die.current_state().loc[3,'Weight'] == 0.01
        
    def test_5_change_weight(self):
        with self.assertRaises(TypeError):
            die = montecarlo.Die(np.array([1,2,3,4,5,6]))
            die.change_weight(3, 'not a number')        
    def test_6_change_weight(self):
        with self.assertRaises(IndexError):
            die = montecarlo.Die(np.array([1,2,3,4,5,6]))
            die.change_weight('not a face', 0)    
            
    def test_7_roll(self):
        die = montecarlo.Die(np.array([1,2,3,4,5,6]))
        assert len(die.roll(12)) == 12

    def test_8_current_state(self):
        die = montecarlo.Die(np.array([1,2,3,4,5,6]))
        assert isinstance(die.current_state(), pd.DataFrame)
        
    def test_9_game_init(self):
        a = montecarlo.Die(np.array([1,2,3,4,5,6]))
        b = montecarlo.Die(np.array([1,2,3,4,5,6]))
        c = montecarlo.Die(np.array([1,2,3,4,5,6]))
        d = montecarlo.Die(np.array([1,2,3,4,5,6]))
        game = montecarlo.Game([a,b,c,d])

        assert all(isinstance(x, montecarlo.Die) for x in game.dice)
        
    def test_10_play(self):
        a = montecarlo.Die(np.array([1,2,3,4,5,6]))
        b = montecarlo.Die(np.array([1,2,3,4,5,6]))
        c = montecarlo.Die(np.array([1,2,3,4,5,6]))
        d = montecarlo.Die(np.array([1,2,3,4,5,6]))
        game = montecarlo.Game([a,b,c,d])
        
        game.play(3)
        played = game.recent_play()
        assert ((len(played.columns) == len(game.dice)) and (len(played.index) == 3))
        
    def test_11_recent_play(self):
        a = montecarlo.Die(np.array([1,2,3,4,5,6]))
        b = montecarlo.Die(np.array([1,2,3,4,5,6]))
        c = montecarlo.Die(np.array([1,2,3,4,5,6]))
        d = montecarlo.Die(np.array([1,2,3,4,5,6]))
        game = montecarlo.Game([a,b,c,d])
        
        game.play(3)
        played = game.recent_play("narrow")   
        assert len(played.columns) == 1
        
    def test_11_recent_play(self):
        with self.assertRaises(ValueError):
            a = montecarlo.Die(np.array([1,2,3,4,5,6]))
            b = montecarlo.Die(np.array([1,2,3,4,5,6]))
            c = montecarlo.Die(np.array([1,2,3,4,5,6]))
            d = montecarlo.Die(np.array([1,2,3,4,5,6]))
            game = montecarlo.Game([a,b,c,d])

            game.play(3)
            played = game.recent_play("not an arg")     
            
    def test_12_analyzer_init(self):
        with self.assertRaises(ValueError):
            a = montecarlo.Analyzer("not a game")
            
    def test_13_jackpot(self):
        a = montecarlo.Die(np.array([1,2]))
        a.change_weight(2,0)
        game = montecarlo.Game([a])

        game.play(20)
        
        analyzer = montecarlo.Analyzer(game)
        
        assert analyzer.jackpot() == 20
        
    def test_14_face_counts_per_roll(self):
        a = montecarlo.Die(np.array([1,2]))
        a.change_weight(2,0)
        game = montecarlo.Game([a])

        game.play(20)
        
        analyzer = montecarlo.Analyzer(game)
        
        assert all(x == 1 for x in analyzer.face_counts_per_roll()[1])
        
    def test_15_combo_count(self):
        a = montecarlo.Die(np.array([1,2,3]))
        b = montecarlo.Die(np.array([1,2,3]))
        game = montecarlo.Game([a,b])

        game.play(500)        
            
        analyzer = montecarlo.Analyzer(game)
        
        assert len(analyzer.combo_count().index) == 6
        
    def test_16_permutation_count(self):
        a = montecarlo.Die(np.array([1,2,3]))
        b = montecarlo.Die(np.array([1,2,3]))      
        game = montecarlo.Game([a,b])

        game.play(500)        
            
        analyzer = montecarlo.Analyzer(game)
        
        assert len(analyzer.permutation_count().index) == 9

    
if __name__ == '__main__':
    
    unittest.main(verbosity=3)  