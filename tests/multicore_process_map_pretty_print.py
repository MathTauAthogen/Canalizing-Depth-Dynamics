import argparse
from multiprocessing import Pool
import datetime
import sys
sys.path.insert(0, '../')
import k_canalyzing_not_faulty as kc
import pyximport
pyximport.install()
import find_attractors_dfs as fad
import time
import array
import numpy
import os.path
import json

#start=time.time()
parser = argparse.ArgumentParser(description='Make a discrete dynamical system at random given the number of variables and canalyzing depth.')
parser.add_argument('num', type= int)
parser.add_argument('cores', type=int)
parser.add_argument('num_vars', type= int)
parser.add_argument('canalyzing_depth', type=int)
args = parser.parse_args()

def threadfunc(placeholder):
    funcs=[]
    for i in range(args.num_vars):
        funcs.append(kc.random_k_canalyzing(args.num_vars, args.canalyzing_depth).return_truth_table())
    tuples=fad.find_attractors_and_basins(funcs)
    return tuples
    #with open("num_vars="+str(args.num_vars)+"_depth="+str(args.canalyzing_depth)+".txt", "a") as file:
    #    print >>file, str(tuples)

start=time.time()
pool = Pool(args.cores)
outputs=pool.map(threadfunc, xrange(args.num))
filename="num_vars="+str(args.num_vars)+"_depth="+str(args.canalyzing_depth)+".json"
loaded=[]
if(os.path.exists(filename)):
	with open(filename, "r") as file:
		loaded=json.load(file)
with open(filename, "w") as file:
    loaded+=outputs
    loaded='[\n'+',\n'.join([json.dumps(i) for i in loaded])+'\n]'
    file.write(loaded)
end=time.time()
print(end-start)
#end=time.time()
#print(end-start)