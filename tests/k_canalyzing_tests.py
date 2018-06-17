"""Program to test validity of functions for randomly creating k-canalyzing functions"""
import matplotlib.pyplot as plt
import scipy.stats as sps
from time import time
import pyximport
import sys
pyximport.install()
sys.path.insert(0, '../')
import partition
import k_canalyzing_faulty as kc

def partition_test(num_vars, num_points):
    """Method to test uniformity of random partitions"""
    data = dict()
    for _ in range(int(partition.fubini(num_vars)) * num_points):
        variables = range(num_vars)
        part = partition.random_partition(variables)
        key = " ".join(["".join([str(j) for j in i]) for i in part])
        if key in data:
            data[key] += 1
        else:
            data[key] = 1
    data_list = data.values()
    plt.bar(range(len(data)), list(data.values()), align='center')
    difference = len(data) - partition.fubini(num_vars)
    print "Found number of functions - number of desired functions : " + str(difference)
    print sps.chisquare(data_list)
    plt.show()

def k_canalyzing_test(num_vars, depth, num_points):
    """Method to test distribution of random_k_canalyzing"""
    data = dict()
    data1 = dict()
    for _ in range(num_points * (2 ** num_vars)):
        func = kc.random_k_canalyzing(num_vars, depth)
        table = func[0].return_truth_table()
        key = "".join([str(i) for i in table])
        if key in data:
            data[key] += 1
        else:
            data[key] = 1
        #Debugging
        key = func[1]
        if key in data1:
            data1[key] += 1
        else:
            data1[key] = 1
    data_list = data.values()
    data1_list = data1.values()
    plt.bar(range(len(data)), list(data.values()), align='center')
    plt.bar(range(len(data1)), list(data1.values()), align='center')
    print "Functions found: " + str(len(data))
    print sps.chisquare(data_list)
    for i in data:
        print i + "  " + str(data[i])
    plt.show()
    
## Test case ##
#partition_test(5, 100)
start = time()
k_canalyzing_test(2, 2, 10000)
end = time()
print(end-start)
