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
    for i in range(len(functions[0])):
        # i = list([int(j) for j in binary_fixed_length(i, int(math.log(len(functions[0]), 2)))])
        i = [int(j) for j in dds.binary_fixed_length(i, int(math.log(len(functions[0]), 2)))]
        if scour(i, attractors_and_bassinets, 3):
            continue
        else:
            dynamic = dds.Dynamical(i[:], functions_formatted)
            oldstates = [i[:]]
            dynamic.iterate()
            while not (dynamic.current in oldstates or scour(
                    dynamic.current, attractors_and_bassinets, 3)):
                oldstates.append(dynamic.current)
                dynamic.iterate()
            if dynamic.current in oldstates and not scour(
                    dynamic.current, attractors_and_bassinets, 3):
                new_attractor = oldstates[oldstates.index(dynamic.current):]
                attractors_and_bassinets[0].append(new_attractor)
                new_bassinet = oldstates
                attractors_and_bassinets[1].append(new_bassinet)
            elif scour(dynamic.current, attractors_and_bassinets[0], 2):
                new_bassinet = oldstates
                index = scan(dynamic.current, attractors_and_bassinets[0], 2)
                attractors_and_bassinets[1][index] = mergelists(
                    attractors_and_bassinets[1][index], new_bassinet)
            else:
                new_bassinet = oldstates
                index = scan(dynamic.current, attractors_and_bassinets[1], 2)
                attractors_and_bassinets[1][index] = mergelists(
                    attractors_and_bassinets[1][index], new_bassinet)
    for i in range(len(attractors_and_bassinets[0])):
        for j in attractors_and_bassinets[0][i]:
            dds.remove(attractors_and_bassinets[1][i], j)
    tuples = []
    for i in range(len(attractors_and_bassinets[0])):
        tuples.append([len(attractors_and_bassinets[0][i]), len(attractors_and_bassinets[1][i])])
    return tuples



#BEGIN TESTING CODE
#print get_attractors_and_bassinets([[0, 0, 0, 1], [0, 1, 1, 1]])
#END TESTING CODE
