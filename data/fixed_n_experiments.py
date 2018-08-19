import argparse
import json
import matplotlib.pyplot as plt
import math
import numpy as np

#--------------------------------------------------------------------------------------------------------

def get_filename(num_vars, canalyzing_depth):
    return "num_vars=" + str(num_vars) + "_depth=" + str(canalyzing_depth) + ".json"

def log_if_possible(x):
#    return math.log(x) if x!=0 else 0
    return x

def plot_function(f, num_vars, f_name):
    x_data = range(num_vars,-1,-1)
    y_data = []
    for canalyzing_depth in x_data:
        with open(get_filename(num_vars, canalyzing_depth), "r") as file:
            data = json.load(file)
            y_data.append(f(data))
    y_data=[log_if_possible(i) for i in y_data]
    plt.plot(x_data, y_data, color='green', marker='o')
    plt.plot([0], [0], color='white')
#    plt.title(f_name + ", number of variables = " + str(num_vars) + ".\n Number of samples = " + str(len(data))) 
    plt.show()

def attractor_one(data):
    counter = 0
    total = 0.0
    for dds in data:
        counter+=len([i for i in dds if i[0]==1])
        total+=len(dds)
    return counter/total

#Run main
#BEGIN
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Plot things.')
    parser.add_argument('num_vars', type= int)
    args = parser.parse_args()
    plot_function(attractor_one, args.num_vars, "Steady states")
#END
