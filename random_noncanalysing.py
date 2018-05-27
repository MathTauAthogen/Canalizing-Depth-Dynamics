"""Generates a random noncanalysing function."""

#Import statements
import math
import random
import time
import boilerplate as bp

#Boilerplates

def rand_string(length):
    """Genererates a random binary string of length length.
    Output format notes:
    Outputs a list representing a binary string.
    """
    k = random.randint(0, 2 ** length - 1)
    return map(int, list(bp.binary_fixed_length(k, length)))

def near_rand_string(length, exceptions):
    """Generates a random binary string of length length that is not any of the exceptions.
    Input format notes:
    exceptions as a list of lists representing binary strings.
    Output format notes:
    Outputs a list representing a binary string."""
    possibilities = bp.invert(exceptions, length)
    try:
        index = random.randint(0, len(possibilities) - 1)
    except ValueError:
        index = 0
    return possibilities[index]

def get_first_vals_list(num, val):
    """Generates a list of lists denoting when the variable number list-index is val."""
    num = 2 ** num
    my_rows = []
    for k in range(num):
        my_rows.append(list(
            [int(i)for i in bp.binary_fixed_length(k, int(math.log(num, 2)))]))
    outerlist = []
    for i in range(int(math.log(num, 2))):
        innerlist = []
        for j in range(num):
            if my_rows[j][i] == val:
                innerlist.append(j)
        outerlist.append(innerlist)
    return outerlist

def is_uniform(my_list):
    """Checks to see if a list only consists of one distinct element."""
    try:
        initial = my_list[0]
        for _, val in enumerate(my_list):
            if val != initial:
                return False
        return True
    except IndexError:
        return False #Needed specifically for this program to default here

def overwrite_at(my_list, index, seq):
    """Overwrites elements my_list starting from index using seq as a template"""
    for i, val in enumerate(seq):
        my_list[index + i] = val

#Main function
def random_noncanalysing_func(num_vars):
    """Generates a random non-canalysing function on num_vars variables.
    Output format notes:
    It outputs a class with the format we agreed upon.
    """
    table = [-1] * (2 ** num_vars)
    first_vals_zero = get_first_vals_list(num_vars, 0)
    first_vals_one = get_first_vals_list(num_vars, 1)
    counter = 2 ** num_vars
    place = 0
    for i in range(num_vars):
        counter = int(counter / 2)
        tempo = [table[a] for a in first_vals_zero[i]]
        temp = []
        for j in tempo:
            if j != -1:
                temp.append(i)
        if is_uniform(temp):
            try:
                overwrite_at(
                    table, place, near_rand_string(counter, [[0] * counter, [1] * counter]))
                place += counter
            except IndexError:
                overwrite_at(table, place, [bp.binary_not(temp[0])])
                place += counter
        else:
            overwrite_at(table, place, rand_string(counter))
            place += counter
    first_ones = [table[i] for i in first_vals_one[0]][:-1]
    if is_uniform(first_ones):
        table[-1] = 1 if first_ones[0] == 0 else 0
    else:
        table[-1] = random.randint(0, 1)
    #Fix up stuff here
    already_changed = []
    ready = False
    while not ready:
        ready = True
        for i in range(num_vars):
            counter = int(counter / 2)
            temp = [table[a] for a in first_vals_one[i]]
            if is_uniform(temp):
                ready = False
                to_sort = first_vals_one[i]
                to_sort.sort()
                for j in already_changed:
                    bp.remove(to_sort, j)
                table[to_sort[-1]] = bp.binary_not(table[to_sort[-1]])
    #End in-progress section
    return bp.Truth(table)

#Testing
START_TIME = time.time()
print random_noncanalysing_func(6).return_truth_table()
END_TIME = time.time()
print END_TIME-START_TIME
