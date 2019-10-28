"""Program for generating ordered partitions of a set"""
import random
import scipy.special as sp

def fubini(elements):
    precomputed = [1, 1, 3, 13, 75, 541, 4683, 47293, 545835, 7087261, 102247563, 1622632573, 28091567595, 526858348381, 10641342970443, 230283190977853, 5315654681981355, 130370767029135901]
    if elements < len(precomputed):
      return precomputed[elements]

    results = [0] * (elements + 1)
    results[0] = 1
    for i in range(1, elements + 1):
        for j in range(1, i + 1):
            results[i] += sp.binom(i, j) * results[i - j]
    return results

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
    fubini_list = fubini(k)
    possibilities = fubini_list[k]
    chooser = random.randint(1, possibilities)
    counter = 0
    count = 0
    while counter < chooser:
        count += 1
        counter += fubini_list[k - count] * sp.binom(k, count)
    subset = random_subset(variables, count)
    left = random_partition(variables)
    left.append(subset)
    return left
