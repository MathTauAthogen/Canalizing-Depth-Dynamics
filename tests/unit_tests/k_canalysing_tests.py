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
import numpy as np

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
        table = func.return_truth_table()
        key = "".join([str(i) for i in table])
        if key in data:
            data[key] += 1
        else:
            data[key] = 1
    data_list = data.values()
    return [data_list, sps.chisquare(data_list)]

def systematic_k_test(max_vars, num_points):
    """Systematically tests each function type with at most max_vars variables"""
    data = dict()
    for i in range(max_vars + 1):
        for j in range(i + 1):
            key = str(i) + " " + str(j)
            data[key] = k_canalyzing_test(i, j, num_points)
    return min([i[1][1] for i in data.values()])
def partition_test(num_vars, num_points):
    """Method to test uniformity of random rp."""
    data = dict()
    for _ in range(int(rp.fubini(num_vars)) * num_points):
        variables = range(num_vars)
        part = rp.random_partition(variables)
        key = " ".join(["".join([str(j) for j in i]) for i in part])
        if key in data:
            data[key] += 1
        else:
            data[key] = 1
    data_list = data.values()
    plt.bar(range(len(data)), list(data.values()), align='center')
    difference = len(data) - rp.fubini(num_vars)
    return difference

class Tests(unittest.TestCase):
    def setUp(self):
        pass
    def test_subset(self):
        self.assertLess(sps.variation(subset_test(3, 2)), 0.1)
    def test_systematic_k(self):
        self.assertGreater(systematic_k_test(3, 100000), 0.05)
    def test_all_partitions_present(self):
        self.assertEqual(partition_test(5, 100),0.0)

if __name__=='__main__':
    unittest.main()
