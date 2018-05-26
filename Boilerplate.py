
"""
This is my boilerplate code.
"""

import math


def binary(myint):
	return "{0:b}".format(myint)


def binary_fixed_length(myint, length):
	return binary(myint).zfill(length)


class truth:
	def __init__(self, table):
		self.table = table

		self.n = len(self.table)

		if (math.log2(self.n).is_integer()):
			pass
		else:
			raise Exception(
			    "No. Just no. You have to pass in a function representation of valid length!"
			)

		self.myrows = []

		for k in range(self.n):
			self.myrows.append(
			    list([
			        int(i)
			        for i in binary_fixed_length(k, int(math.log2(self.n)))
			    ]))

	def function_format(
	    self, row):  #returns -1 upon failure or else the correct 0 or 1 value.
		try:
			i = self.myrows.index(row)
			return self.table[i]
		except:
			return -1

	def return_truth_table(self):
		return self.table


print("F1RST P0ST: " + str(truth([0, 1]).function_format(
    [1])))  #My first test: I'm using your format.

#Okay, now starting to make an object first.
a = truth([0, 0, 0, 0, 1, 0, 1, 1])
print(a.function_format([0, 0, 0]))
print(a.function_format([0, 1, 0]))
print(a.function_format([1, 0, 0]))
print(a.function_format([0, 0, 1]))
print(a.function_format([1, 1, 1]))

#function_format can be abbreviated in the class definition to increase the savings using this method.

#This will also be better for the second subproblem, because in so doing we are able to, instead of plugging in indices of the function, set one of the variables and then vary the others by iterating through all possible numbers between 1 and 2^{n-1} and converting them to binary and then essentially placing them around the fixed value. For example, in three variables with the second fixed at 0, we get 1 = 01 --> [0,0,1] and 2 = 10 --> [1,0,0], etc. A way we could do this of course could be first to get the number into a list, then insert the right value at the right spot using a list operation.

#I would think it could go like the following:
#
#
#goodEggs = [] #Stores all good functions
#
#a = truth(v) #This varies in real code to give all functions of a certain number of variables
#
#index = 0 #in real code would vary
#fixed_val = 0 #in real code would also vary
#
#m = int(log2(n))
#
#isGood = True #in real code, reset every iteration
#isFixed = None #also resets every iteration in real code
#
#for i in range(2^{m-1}):
#   array = [int(i) for i in list(binary_fixed_length(i, m - 1))]
#   array.insert(index, fixed_val)
#   #use as needed here
#   #example of usage:
#   if(isFixed == None):
#       isFixed = a.function_format(array)
#   else:
#       if(isFixed != a.function_format(array)):
#          isGood = False
#if(isGood):
#   goodEggs.append(array)
