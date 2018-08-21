"""Program to test validity of functions for randomly creating k-canalyzing functions"""
from time import time
import sys
import pyximport
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
pyximport.install()
sys.path.insert(0, '../../core')
import random_partition as rp
import generate_k_canalyzing as kc
import unittest

def subset_test(num_vars, size):
    """Method to test uniformity of random partition."""
    data = dict()
    for _ in range(10000):
        variables = range(num_vars)
        part = rp.random_subset(variables, size)
        key = " ".join(map(str, part))
        if key in data:
            data[key] += 1
        else:
            data[key] = 1
    return data.values()

def k_canalyzing_test(num_vars, depth, num_points):
    """Method to test distribution of random_k_canalyzing"""
    data = dict()
    #data1 = dict()
    for _ in range(num_points):
        func = kc.random_k_canalyzing(num_vars, depth)
        #table = func[0].return_truth_table()
        table = func.return_truth_table()
        key = "".join([str(i) for i in table])
        if key in data:
            data[key] += 1
        else:
            data[key] = 1
    data_list = data.values()
    return sps.chisquare(data_list)

def systematic_k_test(max_vars, num_points):
    """Systematically tests each function type with at most max_vars variables"""
    data = dict()
    for i in range(max_vars + 1):
        for j in range(i + 1):
            key = str(i) + " " + str(j)
            data[key] = k_canalyzing_test(i, j, num_points)
    return data.values()

## Test cases ##
#subset_test(3, 2)
#start = time()
#k_canalyzing_test(3, 2, 10000)
#end = time()
#print(end-start)
#start = time()
#systematic_k_test(4, 10000)
#end = time()
#print end - start

class Tests(unittest.TestCase):
    def setUp(self):
        pass
    def test_subset(self):
        self.assertLess(sps.variation(subset_test(3,2)), 0.1)

if __name__=='__main__':
    unittest.main()
