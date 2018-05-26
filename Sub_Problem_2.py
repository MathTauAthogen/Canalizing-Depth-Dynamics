"""
This is my code for sub-problem 2.
"""

import math

def invert(strings, length):
  temp = []
  for k in range(2**length):
    test = list([int(i) for i in binary_fixed_length(k, length)])
    if(test not in strings):
      temp.append(test)
  return temp


def binary(myint):
    return "{0:b}".format(myint)

def binary_fixed_length(myint,length):
    return binary(myint).zfill(length)

class dynamical:
  def __init__(self, initial, functions):
    self.initial = initial
    self.functions = functions
    self.current = initial
  def iterate(self):
    now = self.current
    temp = [-1] * len(self.functions)
    for i in range(len(self.functions)):
      temp[i] = self.functions[i].function_format(now)
    self.current = temp[:]

class truth:
    def __init__(self, table):
        self.table = table
    
        self.n = len(self.table)
        
        if(math.log2(self.n).is_integer()):
            pass
        else:
            raise Exception("No. Just no. You have to pass in a function representation of valid length!")
        
        self.myrows = []
        
        for k in range(self.n):
            self.myrows.append(list([int(i) for i in binary_fixed_length(k, int(math.log2(self.n)))]))
    
    
    def function_format(self, row):#returns -1 upon failure or else the correct 0 or 1 value.
        try:
            i = self.myrows.index(row)
            return self.table[i]
        except:
            return -1
        
    def return_truth_table(self):
        return self.table

#function_format can be abbreviated in the class definition to increase the savings using this method.

#This will also be better for the second subproblem, because in so doing we are able to, instead of plugging in indices of the function, set one of the variables and then vary the others by iterating through all possible numbers between 1 and 2^{n-1} and converting them to binary and then essentially placing them around the fixed value. For example, in three variables with the second fixed at 0, we get 1 = 01 --> [0,0,1] and 2 = 10 --> [1,0,0], etc. A way we could do this of course could be first to get the number into a list, then insert the right value at the right spot using a list operation.

def solve(n):
  goodEggs = []
  for v in range(2**2**n):
    v = list([int(i) for i in binary_fixed_length(v, 2**n)])
    a = truth(v)
    totalGood = False
    for index in range(n):
      for fixed_val in range(2):
        isGood = True
        isFixed = None
        for i in range(2**(n - 1)):
          array = [int(j) for j in list(binary_fixed_length(i, n - 1))]
          array.insert(index, fixed_val)
          if(isFixed == None):
              isFixed = a.function_format(array)
          else:
              if(isFixed != a.function_format(array)):
                isGood = False
        if(isGood):
          totalGood = True
    if(totalGood):
      goodEggs.append(v)
  goodEggs = invert(goodEggs,2**n)
  print(len(goodEggs))
  return goodEggs

print(solve(3))