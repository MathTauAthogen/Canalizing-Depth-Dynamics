import ast
import argparse
import numpy as np
import matplotlib.pyplot as plt
import json
import math

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
      total += sum([att[0] for att in dds]) * 1. / len(dds) 

    return total / len(data)

def avg_attractor_count(data):
    return sum( map(len, data) ) * 1. / len(data)

def avg_total_attractors_size(data):
    total = 0
    for dds in data:
      total += sum([att[0] for att in dds])
    return total * 1. / len(data)

def attractor_one(data):
    counter = 0
    total = 0.0
    for dds in data:
        counter += len([i for i in dds if i[0] == 1])
        total += len(dds)
    return counter / total

#--------------------------------------------------Plot the functions---------------------------------------------------------------------------------------------------

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = 'Plot things some functions of the canalizing depth given that the number of variables is fixed')
    parser.add_argument('num_vars', type = int)
    args = parser.parse_args()
    functions = {
      "Average size of an attractor" : avg_attractor_size,
      "The number of attractors" : avg_attractor_count,
      "Total attractor size" : avg_total_attractors_size,
      "Proportion of steady states" : attractor_one
    }
    for name, func in functions.iteritems():
      plot_function(func, args.num_vars, name)
    
