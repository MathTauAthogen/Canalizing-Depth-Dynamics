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

#--------------------------------------------------3.1-----------------------------------------------------------------------------------------------------------------

def get_filename(num_vars, canalyzing_depth):
    return "../data/num_vars=" + str(num_vars) + "_depth=" + str(canalyzing_depth) + ".json"

def plot_function(f, num_vars, f_name):
    x_data = range(num_vars + 1)
    y_data = []
    for canalyzing_depth in x_data:
        with open(get_filename(num_vars, canalyzing_depth), "r") as file:
            data = json.load(file)
            y_data.append(f(data))
    plt.plot(x_data, y_data, marker="o", color="green")
    plt.title(f_name + ", number of variables = " + str(num_vars) + ".\n Number of samples = " + str(len(data))) 
    plt.show()

def avg_attractor_size(data):
    total = 0
    for dds in data:
      total_attractors = 0
      for att in dds:
        total_attractors += att[0]
      total += total_attractors * 1. / len(dds) 

    return total / len(data)

def avg_attractor_count(data):
    return sum( map(len, data) ) * 1. / len(data)

def avg_total_attractors_size(data):
    total = 0
    for dds in data:
      total += sum( map(lambda att: att[0], dds) )
    return total * 1. / len(data)

def attractor_one(data):
    counter = 0
    total = 0.0
    for dds in data:
        counter+=len([i for i in dds if i[0]==1])
        total+=len(dds)
    return counter/total

#--------------------------------------------------3.2-----------------------------------------------------------------------------------------------------------------

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
    functions = {
      "Average size of an attractor": avg_attractor_size,
      "The number of attractors": avg_attractor_count,
      "Total attractor size": avg_total_attractors_size,
      "Proportion of steady states": attractor_one
    }
    for name, func in functions.iteritems():
      plot_function(func, args.num_vars, name)
    
    for depth in range(args.num_vars):
        main(args.num_vars,depth)
        plotall(args.num_vars)
