"""Generates a random noncanalysing function."""

#Import statements
import math
import random

#Boilerplates
def binary(myint):
    """Returns the binary representation of myint as a string."""
    return "{0:b}".format(myint)

def binary_fixed_length(myint, length):
    """ Returns a zero-padded (of length length) binary representation of myint"""
    return binary(myint).zfill(length)

def rand_string(length):
    """Genererates a random binary string of length length.
    Output format notes:
    Outputs a list representing a binary string.
    """
    k = random.randint(0, 2 ** length - 1)
    return map(int, list(binary_fixed_length(k, length)))

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

def near_rand_string(length, exceptions):
    """Generates a random binary string of length length that is not any of the exceptions.
    Input format notes:
    exceptions as a list of lists representing binary strings.
    Output format notes:
    Outputs a list representing a binary string."""
    string = rand_string(length)
    while True:
        try:
            _ = exceptions.index(string) #Fails if string isn't an exception, and then breaks.
            string = rand_string(length) #Never gets reached if the first line fails.
        except ValueError:
            break
    return string

#Main function
def random_noncanalysing_func(numvars):
    """Generates a random non-canalysing function on numvars variables.
    Output format notes:
    It outputs as a class with the format we agreed upon.
    """
    table = []
    return Truth(table)

#Testing
print random_noncanalysing_func(3)
