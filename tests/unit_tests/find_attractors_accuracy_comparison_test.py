import time
import pyximport
pyximport.install()
import random
import numpy as np
import unittest
import sys
sys.path.insert(0, '../../core')
import find_attractors as fa2
import find_attractors_old as fa

def random_function(degree):
    """Generates a random function in n variables"""
    function = [0] * 2 ** degree
    for i, _ in enumerate(function):
        function[i] = random.randint(0, 1)
    return function

def isPermutation(lista, listb):
    #Use a bijection
    isAPermutation = True
    for i in lista:
        if i not in listb:
            isAPermutation = False        
    for i in listb:
        if i not in lista:
            isAPermutation = False
    return isAPermutation

class Tests(unittest.TestCase):
    def setUp(self):
        pass
    def test_checksout(self):
        cases = 100
        n = 10
        num = 1
        flag = True
        for j in range(num):
            function_list = [np.matrix(
                [random_function(n) for j in range(n)]) for j in range(cases)]#Move in or out
            for i in range(cases):
    	        calculations = fa.FindAttractors(function_list[i])
    	        answer_1 = calculations.get_attractors_and_bassinets()
    	        answer_2 = fa2.find_attractors_and_basins(function_list[i])
                if not isPermutation(answer_1, answer_2):
                   flag=False
        self.assertEqual(flag,True)

if(__name__=="__main__"):
    unittest.main()
