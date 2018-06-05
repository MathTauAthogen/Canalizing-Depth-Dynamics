import time
import pyximport
pyximport.install()
import find_attractors_dfs as fa
import sub_problem_1_runtime_test_non_dfs
import random
import numpy as np
#from random_function import random_function

def random_function(degree):
    """Generates a random function in n variables"""
    function = [0] * 2 ** degree
    for i, _ in enumerate(function):
        function[i] = random.randint(0, 1)
    return function

cases = 100
n = 10
num = 1
start = time.time()
for j in range(num):
    function_list = [np.matrix(
        [random_function(n) for j in range(n)]) for j in range(cases)]#Move in or out
    for i in range(cases):
    	#calculations = fa.FindAttractors(function_list[i])
    	#calculations.get_attractors_and_bassinets()
    	fa.find_attractors_and_basins(function_list[i])
end = time.time()
print (end-start)/num