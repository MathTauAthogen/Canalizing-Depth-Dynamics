"""This is for graphing a bunch of random noncanalysing functions."""
import matplotlib.pyplot as plt
import pyximport
import time
pyximport.install()
import unittest
import sys
sys.path.insert(0, '../../core')
import discrete_dynamical_system as bp
import random_noncanalysing as rnc

def intersect(list_1, list_2):
	totallist = []
	for i in list_1:
		if i in list_2:
			totallist.append(i)
	return totallist

def main(num, amount):
    """Does a distribution with num data points"""
    start = time.time()
    data = [int(''.join(map(str, rnc.random_noncanalysing_func(amount).return_truth_table())), 2) for i in range(num)]
    end = time.time()
    return (end-start)/num

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_large(self):
        n = 3
        self.assertLess(main(138 * 1000, n),0.001)

    def test_small(self):
        n = 2
        self.assertLess(main(1000, n),0.001)

if __name__=='__main__':
    unittest.main()
