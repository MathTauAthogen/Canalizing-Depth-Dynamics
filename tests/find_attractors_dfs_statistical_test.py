import time
import pyximport
pyximport.install()
import random
from math import factorial, fabs
import numpy as np
import unittest

import sys
sys.path.insert(0, '../')
import find_attractors_dfs as fa

def random_function(num_vars):
    """Generates a random function in num_vars variables"""
    function = [0] * 2 ** num_vars
    for i, _ in enumerate(function):
        function[i] = random.randint(0, 1)
    return function

def get_avg_attrcators_count(num_vars, runs):
    total = 0
    for _ in range(runs):
        dds = np.matrix([random_function(num_vars) for i in range(num_vars)])
        attractors = fa.find_attractors_and_basins(dds)
        total = total + len(attractors)
    return total * 1. / runs

def predict_avg_attractor_count(num_vars):
    result = 0
    for size in range(2 ** num_vars, 0, -1):
      result = result + ( factorial(2 ** num_vars) / (factorial(2 ** num_vars - size) * size) ) * 1. / 2 ** (num_vars * size)
    return result

class TestAttractorsStat(unittest.TestCase):
    def setUp(self):
        pass

    def test_stat(self):
        for num_vars in range(1, 8):
            self.assertLess( fabs(get_avg_attrcators_count(num_vars, 3000) - predict_avg_attractor_count(num_vars)), 0.1 )
    def test_size_2(self):
        self.assertEqual(fa.find_attractors_and_basins(np.matrix([[0, 0, 0, 1], [0, 1, 1, 1]])), [[1, 1],[1, 2],[1, 1]])
 

if __name__ == '__main__':
    unittest.main()
