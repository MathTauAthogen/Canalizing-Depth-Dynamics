"""
Finding attractors and bassinets for a discrete dynamical system
"""

import math
import discrete_dynamical_system as dds

def mergelists(my_list, my_second_list):
    """Merge two lists"""
    newlist = []
    for i in my_list:
        newlist.append(i)
    for elem in my_second_list:
        if elem not in newlist:
            newlist.append(elem)
    newlist.sort()
    return newlist

def scan(thing, array, depth):
    """Gets the index in array that contains thing at its depth-1"""
    if depth > 1:
        is_good = -1
        counter = 0
        for i in array:
            if scan(thing, i, depth - 1) != -1:
                is_good = counter
                break
            counter += 1
        return is_good
    else:
        try:
            return array.index(thing)
        except ValueError:
            return -1

def scour(thing, array, depth):
    """Checks if thing exists at a certain depth in array."""
    if depth > 1:
        is_good = False
        for i in array:
            if scour(thing, i, depth - 1):
                is_good = True
                break
        return is_good
    else:
        try:
            array.index(thing)
            return True
        except ValueError:
            return False

def get_attractors_and_bassinets(functions):#pylint: disable=too-many-branches
    """Gets the attractors and bassinets of the given functions"""
    for _, val in enumerate(functions):
        if math.log(len(val), 2).is_integer():
            pass
        else:
            raise Exception(
                "No. Just no. You have to pass in function representations of valid lengths!")
    for _, val in enumerate(functions):
        if len(functions) == math.log(len(val), 2):
            pass
        else:
            raise Exception(
                "No. Just no. There needs to be the right "
                + "size of functions for the number of variables!")
    functions_formatted = []
    for i in functions:
        functions_formatted.append(dds.Truth(i))
    attractors_and_bassinets = [[], []]
    #Begin in-progress code
    
    #End in-progress code
    tuples = []
    for i in range(len(attractors_and_bassinets[0])):
        tuples.append([len(attractors_and_bassinets[0][i]), len(attractors_and_bassinets[1][i])])
    return tuples



#BEGIN TESTING CODE
#print get_attractors_and_bassinets([[0, 0, 0, 1], [0, 1, 1, 1]])
#END TESTING CODE
