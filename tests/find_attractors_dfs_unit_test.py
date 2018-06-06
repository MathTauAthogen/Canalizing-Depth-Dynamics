import unittest
import pyximport
pyximport.install()

import sys
sys.path.insert(0, '../')
import find_attractors_dfs as fa
import numpy as np

class TestAttractors(unittest.TestCase):
    def setUp(self):
        pass

    def test_size_2(self):
        self.assertEqual(fa.find_attractors_and_basins(np.matrix([[0, 0, 0, 1], [0, 1, 1, 1]])), [[1, 1],[1, 2],[1, 1]])
 
    def test_size_3(self):
        self.assertEqual(fa.find_attractors_and_basins(np.matrix([[0, 0, 0, 1, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 1, 0]])), [[2, 6],[1, 2]])

    def test_more_than_2_attractor_size(self):
        self.assertEqual(fa.find_attractors_and_basins(
        	np.matrix([[0, 0, 0, 0, 0, 0, 1, 1], [0, 1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0]]))
        	, [[4, 6],[2, 2]])

if __name__ == '__main__':
    unittest.main()
