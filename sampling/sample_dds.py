import argparse
from multiprocessing import Pool
import datetime
import sys
sys.path.insert(0, '../core')
import generate_k_canalyzing as kc
import pyximport
pyximport.install()
import find_attractors as fad
import time
import array
import numpy
import os.path
import json
import random

#start=time.time()
parser = argparse.ArgumentParser(description='Make a discrete dynamical system at random given the number of variables and canalyzing depth.')
parser.add_argument('num', type = int)
parser.add_argument('cores', type = int)
parser.add_argument('num_vars', type = int)
parser.add_argument('canalyzing_depth', type = int)
args = parser.parse_args()

def threadfunc(seed):
    random.seed(seed)
    funcs = []
    for i in range(args.num_vars):
        funcs.append(kc.random_k_canalyzing(args.num_vars, args.canalyzing_depth).return_truth_table())
    tuples = fad.find_attractors_and_basins(funcs)
    return tuples

start = time.time()
pool = Pool(args.cores)
filename = "./../data/num_vars=" + str(args.num_vars) + "_depth=" + str(args.canalyzing_depth) + ".json"
loaded = []
if(os.path.exists(filename)):
	with open(filename, "r") as file:
		loaded = json.load(file)
num_already_computed = len(loaded) + 1
outputs = pool.map(threadfunc, xrange(num_already_computed, num_already_computed + args.num))
with open(filename, "w") as file:
    loaded += outputs
    json.dump(loaded, file)
end = time.time()
print(end - start)
