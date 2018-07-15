import argparse
import json
import matplotlib.pyplot as plt

#--------------------------------------------------------------------------------------------------------

def get_filename(num_vars, canalyzing_depth):
    return "num_vars=" + str(num_vars) + "_depth=" + str(canalyzing_depth) + ".json"

def plot_function(f, num_vars, f_name):
    x_data = range(num_vars + 1)
    y_data = []
    for canalyzing_depth in x_data:
        with open(get_filename(num_vars, canalyzing_depth), "r") as file:
            data = json.load(file)
            y_data.append(f(data))
    plt.plot(x_data, y_data)
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

#Run main
#BEGIN
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Plot things.')
    parser.add_argument('num_vars', type= int)
    args = parser.parse_args()
    plot_function(avg_attractor_size, args.num_vars, "Average size of an attractor")
    plot_function(avg_attractor_count, args.num_vars, "The number of attractors")
    plot_function(avg_total_attractors_size, args.num_vars, "Total attractors size")
#END



