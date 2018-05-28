"""
Produces a list of all non-canalyzing functions in num variables
"""

import time
import discrete_dynamical_system as dds



def solve(num):
    """main function"""
    good_eggs = []
    for ind in range(2**(2**num - 1)):#pylint: disable=too-many-nested-blocks
        arr = list([int(i) for i in dds.binary_fixed_length(ind, 2**num)])
        truth = dds.Truth(arr)
        total_good = False
        for index in range(num):
            for fixed_val in range(2):
                is_good = True
                is_fixed = None
                for i in range(2**(num - 1)):
                    array = [int(j) for j in list(dds.binary_fixed_length(i, num - 1))]
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
    good_eggs = dds.invert(good_eggs, 2**num)
    return good_eggs

def conjugate(func):
    """Replaces each element of func with the opposite value"""
    return [(1-func[i]) for i in range(len(func))]

#START_TIME = time.time()
#X = solve(3)
#END_TIME = time.time()
#print X
#print len(X)
#print END_TIME-START_TIME
