"""Program for generating random ordered partitions of a set"""
import random

def choose(elements, size):
    """Returns the number of subsets of a certain size in some number of elements"""
    size = min(size, elements - size)
    result = 1
    for i in range(1, size + 1):
        result *= elements - size + i
        result /= i
    return result

def fubini(elements):
    """Returns the nth Fubini number (ordered Bell number)"""
    if elements == 0:
        return 1
    else:
        result = 0
    for i in range(1, elements + 1):
        result += choose(elements, i) * fubini(elements - i)
    return result



def random_subset(variables, subsize):
    """Generates a random subset of a given size from some number of variables"""
    subset = []
    for _ in range(subsize):
        rand = random.randint(0, len(variables) - 1)
        subset.append(variables[rand])
        del variables[rand]
    subset.sort()
    return subset

def random_partition(variables):
    """Generates a uniformly random ordered partition of given elements"""
    k = len(variables)
    if k == 0:
        return []
    possibilities = fubini(k)
    chooser = random.randint(1, possibilities)
    counter = 0
    count = 0
    while counter < chooser:
        count += 1
        counter += fubini(k - count) * choose(k, count)
    subset = random_subset(variables, count)
    left = random_partition(variables)
    left.append(subset)
    return left
