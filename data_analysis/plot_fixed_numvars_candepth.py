import ast
import argparse
import numpy as np
import matplotlib.pyplot as plt
import json
import math

graphs = []
usedgraphs = []
names = []
depths = []
nextcounter = [0]

def get_filename(num_vars, canalyzing_depth):
    return "../data/num_vars=" + str(num_vars) + "_depth=" + str(canalyzing_depth) + ".json"


def plotall(num_vars):
    for i, val in enumerate(graphs):
        if not (val in usedgraphs):
            depth=depths[nextcounter[0]]
            maxval = max(val)
            newval = val
            plt.subplot()
            plt.title(names[nextcounter[0]] + ",\n Number of samples = " + str(len(newval))+".")
            bar_range = list(set(val))
            bar_range.sort()
            plt.plot(bar_range, [math.log(newval.count(a)) if newval.count(a)!=0 else 0 for a in bar_range], color='green', marker='o')
            usedgraphs.append(newval)
            plt.show()
            nextcounter[0]+=1

def addto(func, vals, name, filename, depth):
    # filename=filename.split("_num")[0]
    newname=name
    if not newname in names:    
        names.append(newname)
        graphs.append([])
        graphs[len(graphs)-1].append(func(vals))
        depths.append(depth)
    else:
        i=names.index(newname)
        graphs[i].append(func(vals))

def main(num_vars, depth):
    filename=get_filename(num_vars,depth)
    with open(filename, "r") as file:
        filel=json.load(file)
        for listform in filel:
            transposed=np.matrix(listform).T
            attractors=transposed[0].tolist()[0]
            basins=transposed[1].tolist()[0]
            addto(lambda x:len(x), attractors, "Number of attractors"  + ", number of variables = " + str(num_vars) + ", canalizing depth = " + str(depth), filename, depth)
    plotall(num_vars)

#--------------------------------------------------Plot the functions---------------------------------------------------------------------------------------------------

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Plot things.')
    parser.add_argument('num_vars', type= int)
    args = parser.parse_args()
    
    for depth in range(args.num_vars):
        main(args.num_vars,depth)
        plotall(args.num_vars)
