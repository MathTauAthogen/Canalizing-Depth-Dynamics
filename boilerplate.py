"""
This is my boilerplate code.
"""
import math


def binary(my_int):
    """Returns the binary representation of my_int as a string."""
    return "{0:b}".format(my_int)


def binary_fixed_length(my_int, length):
    """ Returns a zero-padded (of length length) binary representation of my_int"""
    return binary(my_int).zfill(length)


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

        self.my_rows = []

        for k in range(self.num):
            self.my_rows.append(list(
            	   [int(i)for i in binary_fixed_length(k, int(math.log(self.num, 2)))]))

    def function_format(self, row):  #returns -1 upon failure or else the correct 0 or 1 value.
        """Plug in a row to get the corresponding value of the function"""
        try:
            i = self.my_rows.index(row)
            return self.table[i]
        except ValueError:
            return -1

    def return_truth_table(self):
        """ Get the truth table in our agreed-upon format."""
        return self.table

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
