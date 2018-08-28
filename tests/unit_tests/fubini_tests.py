"""Program to test if partitions match fubini numbers"""
from time import time
import pyximport
import sys
import matplotlib.pyplot as plt
import scipy.stats as sps
pyximport.install()
sys.path.insert(0, '../../core')
import random_partition as rp
import generate_k_canalyzing as kc
import unittest

def partition_test(num_vars):
    num_points=10
    distinct=[]
    for _ in range(int(rp.fubini(num_vars)) * num_points):
        variables = range(num_vars)
        part = rp.random_partition(variables)
        if(part not in distinct):
            distinct.append(part)
    return len(distinct)

def num_canalyzing(n, r):
    num_points = 1000
    distinct = []
    for _ in range(num_points):
        new = kc.random_k_canalyzing(n, r)
        if(new.return_truth_table() not in distinct):
            distinct.append(new.return_truth_table())
    return len(distinct)

class TestAttractors(unittest.TestCase):
    def setUp(self):
        pass

    def test_partitions_fubini(self):
        self.assertEqual(partition_test(5), rp.fubini(5))

    def test_canalyzing_number(self):
        self.assertEqual(num_canalyzing(3, 2), 24)

if __name__ == '__main__':
    unittest.main()
