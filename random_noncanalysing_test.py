"""This is for graphing a bunch of random noncanalysing functions."""
import random_noncanalysing as rnc
import matplotlib.pyplot as plt
import boilerplate as bp
import time

def intersect(list_1, list_2):
	totallist = []
	for i in list_1:
		if i in list_2:
			totallist.append(i)
	return totallist

def main(num, amount):
    """Does a distribution with num data points"""
    plt.subplot()
    plt.title("Random Noncanalysing Function Distribution")
    start = time.time()
    data = [int(''.join(map(str, rnc.random_noncanalysing_func(amount).return_truth_table())), 2) for i in range(num)]
    end = time.time()
    print (end-start)/num
    over = []
    for i in data:
    	if(data.count(i) > 10):
    		if(i not in over):
    			over.append(i)
    over.sort()
    #print(over)
    #print(len(over))
    used = []
    for i in data:
    	if i not in used:
    		used.append(i)
    print(len(used))
    bar_range = [i for i in range(0, 2 ** (2 ** amount))]
    plt.hist(data, bar_range, ec='black')
    plt.show()
    return over

totalover = [bp.binary_fixed_length(k, 8) for k in range(2 ** 8)]
for i in range(5):
	over = main(136 * 10, 3)
	totalover = intersect(totalover, over)
print(totalover)
print(len(totalover))