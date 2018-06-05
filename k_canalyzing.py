"""Program for generating random k-canalyzing functions"""
import random
import partition
import discrete_dynamical_system as dds
import random_noncanalysing as rn

def random_k_canalyzing(num_vars, depth):
    """Method to generate a random k-canalyzing function"""
    initial = random.randint(0, 1)
    variables = [i for i in range(num_vars)]
    canalyzing = partition.random_subset(variables, depth)
    partitioned = partition.random_partition(canalyzing)
    desired = [random.randint(0, 1) for _ in range(depth)]
    core = rn.random_noncanalysing_func(len(variables))
    def evaluator(input_table):
        """Method for evaluating the function to create a truth table"""
        start = 0
        for i, subset in enumerate(partitioned):
            for j in subset:
                if input_table[j] == desired[start]:
                    return (initial + i) % 2
                start += 1
        alternate = [input_table[i] for i in variables]
        return core.function_format(alternate)
    result = []
    for i in range(2 ** num_vars):
        state = [int(j) for j in list(dds.binary_fixed_length(i, num_vars))]
        result.append(evaluator(state))
    return dds.Truth(result)
