"""This is code to generate random dynamical systems and observe their properties"""
import random
import sub_problem_1 as sp

def random_function(degree):
    """Generates a random function in n variables"""
    function = [0] * 2 ** degree
    for i, _ in enumerate(function):
        function[i] = random.randint(0, 1)
    return function

def graph_data(degree, points):
    """Generates histograms describing a large number of dynamical systems"""
    import matplotlib.pyplot as plt
    num_attractors = []
    attractor_sizes = []
    bassinet_sizes = []
    for i in range(points):
        functions = []
        for j in range(degree):
            functions.append(random_function(degree))
        attractor_set = sp.get_attractors_and_bassinets(functions)
        num_attractors.append(len(attractor_set))
        for j in range(num_attractors[i]):
            attractor_sizes.append(attractor_set[j][0])
            bassinet_sizes.append(attractor_set[j][1])
    average_number_of_attractors = sum(num_attractors) / (1.0 * points)
    average_attractor_size = sum(attractor_sizes) / (1.0 * points)
    average_bassinet_size = sum(bassinet_sizes) / (1.0 * points)
    print(average_number_of_attractors)
    bar_range = [i - 0.5 for i in range(min(num_attractors), max(num_attractors) + 2)]
    plt.subplot(3, 1, 1)
    plt.title("Attractor Quantities")
    plt.hist(num_attractors, bar_range, ec='black')
    print(average_attractor_size)
    plt.subplot(3, 1, 2)
    plt.title("Attractor Sizes")

    bar_range = [i - 0.5 for i in range(min(attractor_sizes), max(attractor_sizes) + 2)]
    plt.hist(attractor_sizes, bar_range, ec='black')
    print(average_bassinet_size)
    plt.subplot(3, 1, 3)
    plt.title("Bassinet Sizes")

    bar_range = [i - 0.5 for i in range(min(bassinet_sizes), max(bassinet_sizes) + 2)]
    plt.hist(bassinet_sizes, bar_range, ec='black')
    plt.show()


graph_data(3, 1000)
#1.32
