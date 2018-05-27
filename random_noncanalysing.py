"""Generates a random noncanalysing function."""

#Import statements
import math
import random

#Boilerplates
def binary(my_int):
    """Returns the binary representation of my_int as a string."""
    return "{0:b}".format(my_int)

def binary_fixed_length(my_int, length):
    """ Returns a zero-padded (of length length) binary representation of my_int"""
    return binary(my_int).zfill(length)

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

def get_first_vals_list(num, val):
    """Generates a list of lists denoting when the variable number list-index is val."""
    num = 2 ** num
    my_rows = []
    for k in range(num):
        my_rows.append(list(
            [int(i)for i in binary_fixed_length(k, int(math.log(num, 2)))]))
    outerlist = []
    for i in range(int(math.log(num, 2))):
        innerlist = []
        for j in range(num):
            if my_rows[j][i] == val:
                innerlist.append(j)
        outerlist.append(innerlist)
    return outerlist

def isuniform(my_list):
    """Checks to see if a list only consists of one distinct element."""
    initial = my_list[0]
    for _, val in enumerate(my_list):
        if val != initial:
            return False
    return True

#Main function
def random_noncanalysing_func(num_vars):
    """Generates a random non-canalysing function on num_vars variables.
    Output format notes:
    It outputs a class with the format we agreed upon.
    """
    table = [-1] * (2 ** num_vars)
    first_vals_zero = get_first_vals_list(num_vars, 0)
    first_vals_one = get_first_vals_list(num_vars, 1)
    counter = 2 ** num_vars
    for i in range(num_vars):
        if counter != 1:
            pass
        counter = int(counter / 2)
    return Truth(table)

#Testing
print random_noncanalysing_func(3).return_truth_table()
