"""
Plots critical values of particular functions,
where a critical value for a function and a threshold
is the point at which all values of the function differ
from the final value of the function by no more than a
the multiplicative threshold
"""
import argparse
import json
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline as spline
import plot_fixed_numvars as graphs

def graph_critical(function, max_vars, threshold, function_name):
    """Graphs the critical values of a function at each depth"""
    x_data = range(4, max_vars + 1)
    y_data = []
    for num_vars in range(4, max_vars + 1):
        x_dense = [i / 100. for i in range(100 * num_vars + 1)]
        mini_y_data = []
        for depth in range(num_vars + 1):
            with open(graphs.get_filename(num_vars, depth), "r") as file:
                data = json.load(file)
                mini_y_data.append(function(data))
        interpolator = spline(range(num_vars + 1), mini_y_data)
        y_dense = interpolator(x_dense)
        within_threshold = [False] * len(y_dense)
        errors = get_errors(y_dense)
        for i, error in enumerate(errors):
            if error <= threshold:
                within_threshold[i] = True
        critical = len(within_threshold) - 1
        while critical >= 0 and within_threshold[critical]:
            critical -= 1
        critical += 1
        y_data.append(critical / 100.)
    plt.plot(x_data, y_data, color='green', marker='o')
    full_name = function_name + "\nCritical values for up to " + str(max_vars)
    full_name += " variables" + "\nWith a threshold of " + str(threshold)
    plt.title(full_name)
    plt.show()

def get_errors(dataset):
    """Gets the list of percent errors with respect to the final element"""
    errors = []
    for point in dataset:
        errors.append(abs((point - dataset[-1]) / dataset[-1]))
    return errors

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot things.')
    parser.add_argument('num_vars', type=int)
    parser.add_argument('threshold', type=float)
    args = parser.parse_args()
    functions = {
        "Average size of an attractor" : graphs.avg_attractor_size,
        "The number of attractors" : graphs.avg_attractor_count,
        "Total attractor size" : graphs.avg_total_attractors_size,
        "Proportion of steady states" : graphs.attractor_one
    }
    for name, func in functions.iteritems():
        graph_critical(func, args.num_vars, args.threshold, name)
