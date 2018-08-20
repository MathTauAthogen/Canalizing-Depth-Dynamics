"""Program for generating random k-canalyzing functions"""
import random
import random_partition
import pyximport; pyximport.install()
import discrete_dynamical_system as dds
import random_noncanalysing as rn

def all_numbers_but(exceptions, maxn):
    """Generates a list of all ints besides exceptions less than maxn."""
    k = range(maxn)
    temp = []
    for i in k:
        if i not in exceptions:
            temp.append(i)
    return temp

def random_k_canalyzing(num_vars, depth):
    """Method to generate a random k-canalyzing function"""
    if depth == 0:
        return rn.random_noncanalysing_func(num_vars)
    if num_vars == depth:
        return random_nested(num_vars)
    b = random.randint(0, 1)
    variables = range(num_vars)
    canalyzing = random_partition.random_subset(variables, depth)
    non_canalyzing = all_numbers_but(canalyzing, num_vars)
    M_i = random_partition.random_partition(canalyzing)
    offsets = [random.randint(0, 1) for _ in range(depth)]
    core = rn.random_noncanalysing_func(len(non_canalyzing))
    core_table = core.return_truth_core_table()
    if core_table == [0] * 2 ** len(non_canalyzing):
        return random_k_canalyzing(num_vars, depth)
    if len(M_i[-1]) == 1 and len(M_i) != 1 and core_table == [1] * 2 ** len(non_canalyzing):
        return random_k_canalyzing(num_vars, depth)
    if b == 1 and len(M_i[-1]) == 1 and len(M_i) == 1 and core_table == [1] * 2 ** len(non_canalyzing):
        return random_k_canalyzing(num_vars, depth)

    ####
    def evaluator(input_core_table):
        """Method for evaluating the function to create a truth core_table"""
        start = 0
        for i, subset in enumerate(M_i):
            for j in subset:
                if input_core_table[j] == offsets[start]:
                    return (b + i) % 2
                start += 1
        alternate = [input_core_table[i] for i in non_canalyzing]
        return (core.function_format(alternate)+ b + len(M_i) + 1) % 2
    ####   

    result = []
    for i in range(2 ** num_vars):
        state = [int(j) for j in list(dds.binary_fixed_length(i, num_vars))]
        result.append(evaluator(state))
    return dds.Truth(result)

def random_nested(num_vars):
    """Generates a random nested canalyzing function with the given b value"""
    b = random.randint(0, 1)
    core = 1
    variables = range(num_vars)
    M_i = random_partition.random_partition(variables)
    offsets = [random.randint(0, 1) for _ in range(num_vars)]
    if core == 1:
        if len(M_i) != 1:
            if len(M_i[-1]) == 1:
                return random_nested(num_vars)
        else:
            if len(M_i[-1]) == 1:
                if b == 1:
                    return random_nested(num_vars)
    test_string = str(b) + str(core) + str(M_i) + str(offsets)

    ####
    def evaluator(input_core_table):
        """Method for evaluating the function to create a truth core_table"""
        start = 0
        for i, subset in enumerate(M_i):
            for j in subset:
                if input_core_table[j] == offsets[start]:
                    return (b + i) % 2
                start += 1
        return (core + b + len(M_i) + 1) % 2
    #### 

    result = []
    for i in range(2 ** num_vars):
        state = [int(j) for j in list(dds.binary_fixed_length(i, num_vars))]
        result.append(evaluator(state))
    return dds.Truth(result)
