"""Program to test validity of functions for randomly creating k-canalyzing functions"""
#Note:The functions that are in this file but not run are visual tests that have slight acceptable variations from test to test.
from time import time
import sys
import pyximport
import sys
import matplotlib.pyplot as plt
import scipy.stats as sps
pyximport.install()
sys.path.insert(0, '../../core')
import random_partition as rp
import generate_k_canalyzing as kc
import unittest

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

class TestAttractors(unittest.TestCase):
    def setUp(self):
        pass

    def test_all_partitions_present(self):
        self.assertEqual(partition_test(5, 100),0.0)

if __name__ == '__main__':
    unittest.main()
