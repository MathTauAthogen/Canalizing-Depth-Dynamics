"""
This is my code for sub-problem 1.
"""

import math

def mergelists(a,b):
  newlist=[]
  for i in a:
      newlist.append(i)
  for z in b:
      if z not in newlist:
          newlist.append(z)
  newlist.sort()
  return newlist

def binary(myint):
    return "{0:b}".format(myint)

def binary_fixed_length(myint,length):
    return binary(myint).zfill(length)

def remove(a, b):
    try:
        index = a.index(b)
        a.pop(index)
        remove(a, b)
    except:
        pass


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

def scan(thing, array, depth):
  if(depth > 1):
    isGood = -1
    counter = 0
    for i in array:
      if(scour(thing, i, depth - 1) != -1):
        isGood = counter
      counter += 1
    return isGood
  else:
    try:
      return array.index(thing)
    except:
      return -1
def scour(thing, array, depth):
  if(depth > 1):
    isGood = False
    for i in array:
      if(scour(thing, i, depth - 1) == True):
        isGood = True
    return isGood
  else:
    try:
      array.index(thing)
      return True
    except:
      return False

def get_attractors_and_bassinets(functions):#intakes in agreed-upon format
  for i in range(len(functions)):
    if(math.log2(len(functions[i])).is_integer()):
        pass
    else:
        raise Exception("No. Just no. You have to pass in function representations of valid lengths!")
  for i in range(len(functions)):
    if(len(functions) == math.log2(len(functions[i]))):
      pass
    else:
      raise Exception("No. Just no. There needs to be the right size of functions for the number of variables!")
  functions_formatted = []
  for i in functions:
    functions_formatted.append(truth(i))
  attractors_and_bassinets = [[], []]
  for i in range(len(functions[0])):
     # i = list([int(j) for j in binary_fixed_length(i, int(math.log2(len(functions[0]))))])
      i = [int(j) for j in binary_fixed_length(i, int(math.log2(len(functions[0]))))]
      if(scour(i, attractors_and_bassinets, 2)):
        continue
      else:
        a = dynamical(i[:], functions_formatted)
        oldstates = [i[:]]
        a.iterate()
        while(not(a.current in oldstates or scour(a.current, attractors_and_bassinets, 3))):
          oldstates.append(a.current)
          a.iterate()
        if(a.current in oldstates and not(scour(a.current, attractors_and_bassinets, 3))):
          new_attractor = oldstates[oldstates.index(a.current):]
          attractors_and_bassinets[0].append(new_attractor)
          new_bassinet = oldstates
          attractors_and_bassinets[1].append(new_bassinet)
        elif(scour(a.current, attractors_and_bassinets[0], 2)):
          new_bassinet = oldstates
          index = scan(a.current, attractors_and_bassinets[0], 2)
          attractors_and_bassinets[1][index] = mergelists(attractors_and_bassinets[1][index], new_bassinet)
        elif(scour(a.current, attractors_and_bassinets[1], 2)):
          new_bassinet = oldstates
          index = scan(a.current, attractors_and_bassinets[1], 2)
          attractors_and_bassinets[1][index] = mergelists(attractors_and_bassinets[1][index], new_bassinet)
  for i in range(len(attractors_and_bassinets[0])):
      for j in attractors_and_bassinets[0][i]:
          remove(attractors_and_bassinets[1][i], j)
  print(attractors_and_bassinets)
  tuples = []
  for i in range(len(attractors_and_bassinets[0])):
    tuples.append([len(attractors_and_bassinets[0][i]), len(attractors_and_bassinets[1][i])])
  return tuples



#BEGIN TESTING CODE
print(get_attractors_and_bassinets([[0, 0, 0, 1], [0, 1, 1, 1]]))#The parameter is a list of lists. This can be changed. I do error handling.
#END TESTING CODE
