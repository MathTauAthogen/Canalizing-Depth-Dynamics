"""This is code to generate random dynamical systems and observe their properties"""
import random
import pyximport; pyximport.install()
import find_attractors_dfs as fa
import numpy as np

def random_function(degree):
    """Generates a random function in n variables"""
    function = [0] * 2 ** degree
    for i, _ in enumerate(function):
        function[i] = random.randint(0, 1)
    return function

def get_data(num_vars, points):
    """Generates data sets describing random systems of num_vars variables"""
    result = []
    num_attractors = []
    avg_attractor_sizes = []
    attractor_sizes = []
    basin_sizes = []
    for i in range(points):
        functions = []
        for j in range(num_vars):
            functions.append(random_function(num_vars))
        attractor_set = fa.find_attractors_and_basins(np.matrix(functions))
        num_attractors.append(len(attractor_set))
        attractor_sizes.extend([att[0] for att in attractor_set])
        basin_sizes.extend([att[1] for att in attractor_set])
        avg_attractor_sizes.append( sum([att[0] for att in attractor_set]) / (1. * len(attractor_set)) )
 
    return {
        "num_attractors" : num_attractors,
        "avg_attractor_sizes" : avg_attractor_sizes,
        "attractor_sizes" : attractor_sizes,
        "basin_sizes" : basin_sizes
    }

def graph_data(num_vars, points):
    """Generates histograms describing a large number of dynamical systems"""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    data = get_data(num_vars, points)
    num_attractors = data["num_attractors"]
    avg_attractor_sizes = data["avg_attractor_sizes"]
    attractor_sizes = data["attractor_sizes"]
    basin_sizes = data["basin_sizes"]
    average_number_of_attractors = sum(num_attractors) / (1. * points)
    average_avg_attractor_size = sum(avg_attractor_sizes) / (1. * points)
    average_attractor_size = sum(attractor_sizes) / (1. * len(attractor_sizes))
    average_basin_size = sum(basin_sizes) / (1.0 * len(basin_sizes))
    print("Number of variables: ", num_vars)

    print("Average number of attractors:", average_number_of_attractors)
    bar_range = [i - 0.5 for i in range(min(num_attractors), max(num_attractors) + 2)]
    plt.subplot(4, 1, 1)
    plt.title("Attractor Quantities")
    plt.hist(num_attractors, bar_range, ec='black')

    print("Average attractor size", average_attractor_size)
    plt.subplot(4, 1, 2)
    plt.title("Attractor Sizes")
    bar_range = [i - 0.5 for i in range(2 ** num_vars + 2)]
    plt.hist(attractor_sizes, bar_range, ec='black')

    print("Average average attractor size", average_avg_attractor_size)
    plt.subplot(4, 1, 3)
    plt.title("Average Attractor Sizes")
    bar_range = [i - 0.5 for i in range(2 ** num_vars + 2)]
    plt.hist(avg_attractor_sizes, bar_range, ec='black')


    print("Average basin size", average_basin_size)
    plt.subplot(4, 1, 4)
    plt.title("Basin Sizes")
    bar_range = [i - 0.5 for i in range(2 ** num_vars + 2)]
    plt.hist(basin_sizes, bar_range, ec='black')

    plt.savefig('rf.png')

def graph_growth(degree, points):
    """Graphs the changes in the mean values as the number of variables increases"""
    import matplotlib.pyplot as plt
    attractor_averages = []
    attractor_size_averages = []
    basin_size_averages = []
    x_axis = []
    for i in range(1, degree + 1):
        for _ in range(10):
            x_axis.append(i)
    for i in range(1, degree + 1):
        for _ in range(10):
            data = get_data(i, points)
            average_number_of_attractors = sum(data[0]) / (1.0 * points)
            attractor_averages.append(average_number_of_attractors)
            average_attractor_size = sum(data[1]) / (1.0 * points)
            attractor_size_averages.append(average_attractor_size)
            average_basin_size = sum(data[2]) / (1.0 * points)
            basin_size_averages.append(average_basin_size)
    plt.subplot(3, 1, 1)
    plt.title("Average number of attractors")
    plt.xlabel("degree")
    plt.ylabel("Average number of attractors")
    plt.plot(x_axis, attractor_averages, "ro")
    plt.subplot(3, 1, 2)
    plt.title("Average attractor size")
    plt.xlabel("degree")
    plt.ylabel("Average attractor size")
    plt.plot(x_axis, attractor_size_averages, "ro")
    plt.subplot(3, 1, 3)
    plt.title("Average basin size")
    plt.xlabel("degree")
    plt.ylabel("Average basin size")
    plt.plot(x_axis, basin_size_averages, "ro")
    plt.show()


graph_data(5, 3000000)
#graph_growth(5, 100)
