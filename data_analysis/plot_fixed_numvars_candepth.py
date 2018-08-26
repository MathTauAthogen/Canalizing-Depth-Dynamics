import ast
import argparse
import numpy as np
import matplotlib.pyplot as plt
import json
import math

def get_filename(num_vars, canalyzing_depth):
    return "../data/num_vars=" + str(num_vars) + "_depth=" + str(canalyzing_depth) + ".json"

def plot(num_vars, args):
        val = [] 
        filename=args[2]
        with open(filename, "r") as file:
            filel=json.load(file)
            for i in filel:
                val.append(args[0](i))
        maxval = max(val)
        plt.subplot()
        plt.title(args[1] + ",\n Number of samples = " + str(len(val)) + ".")
        bar_range = list(set(val))
        bar_range.sort()
        plt.plot(bar_range, [math.log(val.count(a)) if val.count(a) != 0 else 0 for a in bar_range], color = 'green', marker = 'o')
        plt.show()

#--------------------------------------------------Plot the functions---------------------------------------------------------------------------------------------------

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = 'Plot things.')
    parser.add_argument('num_vars', type = int)
    parser.add_argument('canalyzing_depth', type = int)
    args = parser.parse_args()
    numvars = args.num_vars
    depth = args.canalyzing_depth
    plot(args.num_vars, [lambda x:len(x), "Number of attractors"  + ", number of variables = " + str(args.num_vars) + ", canalizing depth = " + str(depth), get_filename(args.num_vars,depth)])
