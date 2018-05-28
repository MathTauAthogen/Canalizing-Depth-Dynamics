"""This is code to generate random dynamical systems and observe their properties"""
import random
import find_attractors as fa

def random_function(degree):
    """Generates a random function in n variables"""
    function = [0] * 2 ** degree
    for i, _ in enumerate(function):
        function[i] = random.randint(0, 1)
    return function

def get_data(degree, points):
    """Generates data sets describing random systems of degree n"""
    result = []
    num_attractors = []
    attractor_sizes = []
    bassinet_sizes = []
    for i in range(points):
        functions = []
        for j in range(degree):
            functions.append(random_function(degree))
        attractor_set = fa.get_attractors_and_bassinets(functions)
        num_attractors.append(len(attractor_set))
        for j in range(num_attractors[i]):
            attractor_sizes.append(attractor_set[j][0])
            bassinet_sizes.append(attractor_set[j][1])
    result.append(num_attractors)
    result.append(attractor_sizes)
    result.append(bassinet_sizes)
    return result

def graph_data(degree, points):
    """Generates histograms describing a large number of dynamical systems"""
    import matplotlib.pyplot as plt
    data = get_data(degree, points)
    num_attractors = data[0]
    attractor_sizes = data[1]
    bassinet_sizes = data[2]
    average_number_of_attractors = sum(num_attractors) / (1.0 * points)
    average_attractor_size = sum(attractor_sizes) / (1.0 * points)
    average_bassinet_size = sum(bassinet_sizes) / (1.0 * points)
    print("Number of variables: ", degree)
    print("Average number of attractors:", average_number_of_attractors)
    bar_range = [i - 0.5 for i in range(min(num_attractors), max(num_attractors) + 2)]
    plt.subplot(3, 1, 1)
    plt.title("Attractor Quantities")
    plt.hist(num_attractors, bar_range, ec='black')
    print("Average attractor size", average_attractor_size)
    plt.subplot(3, 1, 2)
    plt.title("Attractor Sizes")

    bar_range = [i - 0.5 for i in range(min(attractor_sizes), max(attractor_sizes) + 2)]
    plt.hist(attractor_sizes, bar_range, ec='black')
    print("Average bassinet size", average_bassinet_size)
    plt.subplot(3, 1, 3)
    plt.title("Bassinet Sizes")

    bar_range = [i - 0.5 for i in range(min(bassinet_sizes), max(bassinet_sizes) + 2)]
    plt.hist(bassinet_sizes, bar_range, ec='black')
    plt.show()

def graph_growth(degree, points):
    """Graphs the changes in the mean values as the number of variables increases"""
    import matplotlib.pyplot as plt
    attractor_averages = []
    attractor_size_averages = []
    bassinet_size_averages = []
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
            average_bassinet_size = sum(data[2]) / (1.0 * points)
            bassinet_size_averages.append(average_bassinet_size)
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
    plt.title("Average bassinet size")
    plt.xlabel("degree")
    plt.ylabel("Average bassinet size")
    plt.plot(x_axis, bassinet_size_averages, "ro")
    plt.show()


graph_data(8, 1000000)
graph_growth(5, 100)
