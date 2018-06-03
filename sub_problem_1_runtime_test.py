import time
import pyximport
pyximport.install(setup_args={"script_args":["--compiler=mingw32"]}, reload_support=True)
import find_attractors as fa
import random
#from random_function import random_function

def random_function(degree):
    """Generates a random function in n variables"""
    function = [0] * 2 ** degree
    for i, _ in enumerate(function):
        function[i] = random.randint(0, 1)
    return function

start = time.time()
n = 10
for i in range(100):
	f  = [random_function(n) for j in range(n)]
	calculations = fa.FindAttractors(f)
	calculations.get_attractors_and_bassinets()
end = time.time()
print end-start
