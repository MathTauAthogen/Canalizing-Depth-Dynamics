"""
This is my boilerplate code.
"""
import math


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

print "F1RST P0ST: " + str(Truth([0, 1]).function_format([1]))

#Okay, now starting to make an object first.
A = Truth([0, 0, 0, 0, 1, 0, 1, 1])
print A.function_format([0, 0, 0])
print A.function_format([0, 1, 0])
print A.function_format([1, 0, 0])
print A.function_format([0, 0, 1])
print A.function_format([1, 1, 1])
