"""
Plots 
"""
import argparse
import json
import matplotlib.pyplot as plt
import plot_fixed_numvars as graphs

def graph_ratios(function, max_vars, function_name):
    """"""
    x_data = range(4, max_vars + 1)
    y_data = []
    for num_vars in range(4, max_vars + 1):
        mini_y_data = []
        for depth in range(2):
            with open(graphs.get_filename(num_vars, depth), "r") as file:
                data = json.load(file)
                mini_y_data.append(function(data))
        y_data.append(float(mini_y_data[1])/mini_y_data[0])
    plt.plot(x_data, y_data, color='green', marker='o')
    full_name = function_name + "\nRatios for up to " + str(max_vars)
    plt.title(full_name)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot things.')
    parser.add_argument('num_vars', type=int)
    args = parser.parse_args()
    functions = {
        "Average size of an attractor" : graphs.avg_attractor_size,
        "The number of attractors" : graphs.avg_attractor_count,
        "Total attractor size" : graphs.avg_total_attractors_size,
        "Proportion of steady states" : graphs.attractor_one
    }
    for name, func in functions.iteritems():
        graph_ratios(func, args.num_vars, name)
