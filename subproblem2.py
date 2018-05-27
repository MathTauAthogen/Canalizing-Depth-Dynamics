"""
This is my code for sub-problem 2.
"""

import math
import time

def invert(strings, length):
    """Outputs a list of all of the binary strings with length digits that aren't in strings."""
    temp = []
    for k in range(2**(length - 1)):
        test = list([int(i) for i in binary_fixed_length(k, length)])
        if test not in strings:
            temp.append(test)
            temp.append(conjugate(test))
    return temp


def binary(myint):
    """Returns the binary representation of myint as a string."""
    return "{0:b}".format(myint)


def binary_fixed_length(myint, length):
    """ Returns a zero-padded (of length length) binary representation of myint"""
    return binary(myint).zfill(length)

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
                [int(i) for i in binary_fixed_length(k, int(math.log(self.num, 2)))]))

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

def solve(num):
    """main function"""
    good_eggs = []
    for ind in range(2**(2**num - 1)):#pylint: disable=too-many-nested-blocks
        arr = list([int(i) for i in binary_fixed_length(ind, 2**num)])
        truth = Truth(arr)
        total_good = False
        for index in range(num):
            for fixed_val in range(2):
                is_good = True
                is_fixed = None
                for i in range(2**(num - 1)):
                    array = [int(j) for j in list(binary_fixed_length(i, num - 1))]
                    array.insert(index, fixed_val)
                    if is_fixed is None:
                        is_fixed = truth.function_format(array)
                    else:
                        if is_fixed != truth.function_format(array):
                            is_good = False
                if is_good:
                    total_good = True
                    break
            if total_good:
                break

        if total_good:
            good_eggs.append(arr)
            good_eggs.append(conjugate(arr))
    good_eggs = invert(good_eggs, 2**num)
    return good_eggs

def conjugate(func):
    """Replaces each element of func with the opposite value"""
    return [(1-func[i]) for i in range(len(func))]

START_TIME = time.time()
X = solve(2)
END_TIME = time.time()
print X
print len(X)
print END_TIME-START_TIME
