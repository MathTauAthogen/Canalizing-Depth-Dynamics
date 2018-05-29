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

def all_numbers_but(exceptions, length):
    """Generates a list of all ints besides exceptions with length <= length in binary."""
    k = range(2 ** length)
    temp = []
    for i in k:
        if i not in exceptions:
            temp.append(i)
    return temp

def binary_list_to_decimal(list):
    """Converts list(a list representing a binary string) to a decimal int"""
    return int(''.join(list), 2)

def backtrack(current_pos, backtrack_array):
    """Backtrack from a point and return all points hit"""
    pass

def get_back_array(states):
    """Given a state-function, find the array of arrays that point to each value"""
    back = [[]] * len(states)
    for i, val in enumerate(states):
        back[val].append(i)
    return back

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
    attractors_and_bassinets = [[], []]
    #Begin in-progress code
    dynamical = dds.Dynamical([0] * len(functions), functions)#Only to get the states function.
    state_function = dynamical.states
    referred_list = list(set(state_function))#Everything that is not only an IC
    initial_conditions = all_numbers_but(referred_list, len(functions))
    back_array = get_back_array(state_function)
    used = []
    for i in initial_conditions:
        if i in used:
            continue
        old_states = []
        current_position = i
        last_state = current_position
        while current_position not in old_states:
            old_states.append(current_position)
            for i in back_array[current_position]:
                if i != last_state:
                    old_states = list(set(old_states + backtrack(i, back_array)))
            last_state = current_position
            current_position = state_function[current_position]
        attractor = [current_position]
        current_position = state_function[current_position]
        while current_position not in attractor:
            attractor.append(current_position)
            current_position = state_function[current_position]
        bassinet = list(set(old_states) - set(attractor))
        attractors_and_bassinets[0].append(attractor)
        attractors_and_bassinets[1].append(bassinet)
    #End in-progress code
    tuples = []
    for i in range(len(attractors_and_bassinets[0])):
        tuples.append([len(attractors_and_bassinets[0][i]), len(attractors_and_bassinets[1][i])])
    return tuples



#BEGIN TESTING CODE
#print get_attractors_and_bassinets([[0, 0, 0, 1], [0, 1, 1, 1]])
#END TESTING CODE
