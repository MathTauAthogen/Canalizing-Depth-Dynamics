"""
Finding attractors and bassinets for a discrete dynamical system
"""

import math
#import discrete_dynamical_system as dds
import pyximport
import sys
pyximport.install()

class Dynamical(object):
    """The class that stores the discrete dynamical system"""
    def __init__(self, initial, functions):
        self.functions = functions
        self.current = initial
        temp = map(list, zip(*functions))
        self.states = [int(''.join(map(str, val)), 2) for _, val in enumerate(temp)]

def get_back_array(states):
    """Given a state-function, find the array of arrays that point to each value"""
    back = []
    for a, b in enumerate(states):
        back.append([])
    for i, val in enumerate(states):
        back[val].append(i)#Appends to all arrays. Why?
    return back

def all_numbers_but(exceptions, length):
    """Generates a list of all ints besides exceptions with length <= length in binary."""
    k = range(2 ** length)
    temp = []
    for i in k:
        if i not in exceptions:
            temp.append(i)
    return temp

class FindAttractors(object):

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
                self.backtrack(j, back_array, old_states_2)
            bassinet = list(old_states_2.keys())
            self.attractors_and_bassinets[1].append(bassinet)
            self.used = list(set(self.used + bassinet))

    def __init__(self, functions):
        self.attractors_and_bassinets = [[], []]
        self.state_function = None
        self.used = []
        self.referred_list = None
        self.functions = functions

    def get_attractors_and_bassinets(self):#pylint: disable=too-many-branches
        """Gets the attractors and bassinets of the given functions"""
        #sys.exit()
        for _, val in enumerate(self.functions):
            if math.log(len(val), 2).is_integer():
                pass
            else:
                raise Exception(
                    "No. Just no. You have to pass in function representations of valid lengths!")
        for _, val in enumerate(self.functions):
            if len(self.functions) == math.log(len(val), 2):
                pass
            else:
                raise Exception(
                    "No. Just no. There needs to be the right "
                    + "size of functions for the number of variables!")
        #Begin in-progress code
        dynamical = Dynamical([0] * len(self.functions), self.functions)#Only to get the states function.
        self.state_function = dynamical.states
        self.referred_list = list(set(self.state_function))#Everything that is not only an IC
        #Loops with branches
        self.handle_loops_with_branches()