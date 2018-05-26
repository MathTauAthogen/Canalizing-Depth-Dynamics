"""
This is my code for sub-problem 1.
"""

import math

def mergelists(lista, listb):
    """Merge two lists"""
    newlist = []
    for i in lista:
        newlist.append(i)
    for elem in listb:
        if elem not in newlist:
            newlist.append(elem)
    newlist.sort()
    return newlist

def binary(myint):
    """Returns the binary representation of myint as a string."""
    return "{0:b}".format(myint)


def binary_fixed_length(myint, length):
    """ Returns a zero-padded (of length length) binary representation of myint"""
    return binary(myint).zfill(length)

def remove(lista, element):
    """ Removes all instances of element from lista"""
    try:
        index = lista.index(element)
        lista.pop(index)
        remove(lista, element)
    except ValueError:
        pass


class Dynamical(object):
    """The class that stores the discrete dynamical system"""
    def __init__(self, initial, functions):
        self.initial = initial
        self.functions = functions
        self.current = initial
    def iterate(self):
        """ Increases the time by 1"""
        now = self.current
        temp = [-1] * len(self.functions)
        for i in range(len(self.functions)):
            temp[i] = self.functions[i].function_format(now)
        self.current = temp[:]
    def placeholder(self):
        """ Not enough public methods otherwise"""
        pass

class Truth(object):
    """This is how I store functions."""
    def __init__(self, table):
        self.table = table
        self.num = len(self.table)
        if math.log(self.num, 2).is_integer():
            pass
        else:
            raise Exception(
                "No. Just no. You have to pass in a function representation of valid length!")

        self.myrows = []

        for k in range(self.num):
            self.myrows.append(list(
                [int(i)for i in binary_fixed_length(k, int(math.log(self.num, 2)))]))

    def function_format(self, row):  #returns -1 upon failure or else the correct 0 or 1 value.
        """Plug in a row to get the corresponding value of the function"""
        try:
            i = self.myrows.index(row)
            return self.table[i]
        except ValueError:
            return -1

    def return_truth_table(self):
        """ Get the truth table in our agreed-upon format."""
        return self.table

def scan(thing, array, depth):
    """Gets the index in array that contains thing at its depth-1"""
    if depth > 1:
        is_good = -1
        counter = 0
        for i in array:
            if scour(thing, i, depth - 1) != -1:
                is_good = counter
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
        functions_formatted.append(Truth(i))
    attractors_and_bassinets = [[], []]
    for i in range(len(functions[0])):
        # i = list([int(j) for j in binary_fixed_length(i, int(math.log(len(functions[0]), 2)))])
        i = [int(j) for j in binary_fixed_length(i, int(math.log(len(functions[0]), 2)))]
        if scour(i, attractors_and_bassinets, 2):
            continue
        else:
            dynamic = Dynamical(i[:], functions_formatted)
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
            elif scour(dynamic.current, attractors_and_bassinets[1], 2):
                new_bassinet = oldstates
                index = scan(dynamic.current, attractors_and_bassinets[1], 2)
                attractors_and_bassinets[1][index] = mergelists(
                    attractors_and_bassinets[1][index], new_bassinet)
    for i in range(len(attractors_and_bassinets[0])):
        for j in attractors_and_bassinets[0][i]:
            remove(attractors_and_bassinets[1][i], j)
    print attractors_and_bassinets
    tuples = []
    for i in range(len(attractors_and_bassinets[0])):
        tuples.append([len(attractors_and_bassinets[0][i]), len(attractors_and_bassinets[1][i])])
    return tuples



#BEGIN TESTING CODE
print get_attractors_and_bassinets([[0, 0, 0, 1], [0, 1, 1, 1]])
#END TESTING CODE
