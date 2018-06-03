"""
Finding attractors and bassinets for a discrete dynamical system
"""

import math
import discrete_dynamical_system as dds
import numpy as np

def all_numbers_but(exceptions, length):
    """Generates a list of all ints besides exceptions with length <= length in binary."""
    k = np.arange(2 ** length)
    return np.delete(k, exceptions)

def binary_list_to_decimal(list):
    """Converts list(a list representing a binary string) to a decimal int"""
    return int(''.join(list), 2)

def backtrack(current_pos, backtrack_array, loop_points):
    """Backtrack from a point and return if there is an attractor and the points hit."""
    loop_points[current_pos] = 1
    for i in backtrack_array[current_pos]:
        if loop_points[i] == 1:
            continue
        backtrack(i, backtrack_array, loop_points)

def get_back_array(states):
    """Given a state-function, find the array of arrays that point to each value"""
    back = []
    for _, _ in enumerate(states):
        back.append([])
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
    #Loops with branches
    for i in initial_conditions:
        if i in used:
            continue
        old_states = dict(zip(range(2 ** len(functions)), [0] * (2 ** len(functions))))
        old_states_array = []
        move = i
        while old_states[move] == 0:
            old_states[move] = 1
            old_states_array.append(move)
            move = state_function[move]
        attractor = old_states_array[old_states_array.index(move):]
        attractors_and_bassinets[0].append(attractor)
        old_states_2 = dict(zip(range(2 ** len(functions)), [0] * (2 ** len(functions))))
        for j in attractor:
            old_states_2[j] = 1
        for j in attractor:
            backtrack(j, back_array, old_states_2)
        bassinet = [k for k, v in old_states_2.items() if v == 1]
        attractors_and_bassinets[1].append(bassinet)
        used = list(set(used + bassinet))
    #Loops without branches
    in_loops = all_numbers_but(used, len(functions))
    used_2 = []
    for i in in_loops:
        if i not in used_2:
            temp = [i]
            moves = state_function[i]
            while moves != i:
                temp.append(moves)
                moves = state_function[moves]
            attractors_and_bassinets[0].append(temp)
            attractors_and_bassinets[1].append(temp)
            used_2 = list(set(used_2 + temp))
    #End in-progress code
    tuples = []
    for i in range(len(attractors_and_bassinets[0])):
        #tuples.append([attractors_and_bassinets[0][i], attractors_and_bassinets[1][i]])
        tuples.append([len(attractors_and_bassinets[0][i]), len(attractors_and_bassinets[1][i])])
    return tuples



#BEGIN TESTING CODE
#print get_attractors_and_bassinets([[0, 0, 0, 1], [0, 1, 1, 1]])
#END TESTING CODE
