"""
Finding attractors and bassinets for a discrete dynamical system
"""

import math
import discrete_dynamical_system as dds
import pyximport
import sys
pyximport.install()

cdef backtrack(int current_pos, backtrack_array, dict loop_points):
    """Backtrack from a point and return if there is an attractor and the points hit."""
    cdef bint attract = False
    cdef bint back_bool = False
    if current_pos in loop_points:
        return True
    loop_points[current_pos] = 1
    for i in backtrack_array[current_pos]:
        back_bool = backtrack(i, backtrack_array, loop_points)
        if back_bool:
            attract = True
    return attract

cdef all_numbers_but(exceptions, int length):
    """Generates a list of all ints besides exceptions with length <= length in binary."""
    k = range(2 ** length)
    temp = []
    cdef int i
    for i in k:
        if i not in exceptions:
            temp.append(i)
    return temp

def binary_list_to_decimal(list):
    """Converts list(a list representing a binary string) to a decimal int"""
    return int(''.join(list), 2)

def get_back_array(states):
    """Given a state-function, find the array of arrays that point to each value"""
    back = []
    for a, b in enumerate(states):
        back.append([])
    for i, val in enumerate(states):
        back[val].append(i)#Appends to all arrays. Why?
    return back

class FindAttractors(object):
    def __init__(self, functions):
        self.attractors_and_bassinets = [[], []]
        self.state_function = None
        self.used = []
        self.referred_list = None
        self.functions = functions

    @classmethod
    def backtrack(cls, current_pos, backtrack_array, loop_points):
        """Backtrack from a point and return if there is an attractor and the points hit."""
        cdef bint attract = False
        cdef bint back_bool = False
        if current_pos in loop_points:
            return True
        loop_points[current_pos] = 1
        for i in backtrack_array[current_pos]:
            back_bool = cls.backtrack(i, backtrack_array, loop_points)
            if back_bool:
                attract = True
        return attract

    def get_attractors_and_bassinets(self):#pylint: disable=too-many-branches
        """Gets the attractors and bassinets of the given functions"""
        # for _, val in enumerate(self.functions):
        #     if math.log(len(val), 2).is_integer():
        #         pass
        #     else:
        #         raise Exception(
        #             "No. Just no. You have to pass in function representations of valid lengths!")
        # for _, val in enumerate(self.functions):
        #     if len(self.functions) == math.log(len(val), 2):
        #         pass
        #     else:
        #         raise Exception(
        #             "No. Just no. There needs to be the right "
        #             + "size of functions for the number of variables!")
        #Begin in-progress code
        dynamical = dds.Dynamical([0] * len(self.functions), self.functions)#Only to get the states function.
        #return
        self.state_function = dynamical.states
        self.referred_list = list(set(self.state_function))#Everything that is not only an IC
        self.handle_loops_with_branches()
        #Loops without branches
        in_loops = all_numbers_but(self.used, len(self.functions))
        used_2 = []
        for i in in_loops:
            if i not in used_2:
                temp = [i]
                moves = self.state_function[i]
                while moves != i:
                    temp.append(moves)
                    moves = self.state_function[moves]
                self.attractors_and_bassinets[0].append(temp)
                self.attractors_and_bassinets[1].append(temp)
                used_2 = list(set(used_2 + temp))
        #End in-progress code
        tuples = []
        for i in range(len(self.attractors_and_bassinets[0])):
            #tuples.append([attractors_and_bassinets[0][i], attractors_and_bassinets[1][i]])
            tuples.append([len(self.attractors_and_bassinets[0][i]), len(self.attractors_and_bassinets[1][i])])
        return tuples

    def handle_loops_with_branches(self):
        initial_conditions = all_numbers_but(self.referred_list, len(self.functions))
        back_array = get_back_array(self.state_function)
        for i in initial_conditions:
            if i in self.used:
                continue
            old_states = {}
            move = i
            counter = 0
            while move not in old_states:
                old_states[move] = counter
                move = self.state_function[move]
                counter += 1
            attractor = [k for k, v in old_states.items() if v >= old_states[move]]
            self.attractors_and_bassinets[0].append(attractor)
            old_states_2 = {}
            for j in attractor:
                backtrack(j, back_array, old_states_2)
            bassinet = list(old_states_2.keys())
            self.attractors_and_bassinets[1].append(bassinet)
            self.used = list(set(self.used + bassinet))



#BEGIN TESTING CODE
#print get_attractors_and_bassinets([[0, 0, 0, 1], [0, 1, 1, 1]])
#END TESTING CODE
