"""Program for generating random k-canalyzing functions"""
import random
import partition
import discrete_dynamical_system as dds
import random_noncanalysing as rn

def random_k_canalyzing(num_vars, depth):
    """Method to generate a random k-canalyzing function"""
    if depth == 0:
        return rn.random_noncanalysing_func(num_vars)
    if num_vars == depth:
        return random_nested(num_vars)
    initial = random.randint(0, 1)
    variables = range(num_vars)
    canalyzing = partition.random_subset(variables, depth)
    partitioned = partition.random_partition(canalyzing)
    desired = [random.randint(0, 1) for _ in range(depth)]
    core = rn.random_noncanalysing_func(len(variables))
#    disallowed = (initial + len(partitioned) + 1) % 2
    if core.return_truth_table() == [(initial + len(partitioned) + 1) % 2] * 2 ** len(variables):
        return random_k_canalyzing(num_vars, depth)
    table = core.return_truth_table()
    if len(partitioned) != 1 and len(partitioned[-1]) == 1 and table == [1] * 2 ** len(variables):
        return random_k_canalyzing(num_vars, depth)
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

#print random_k_canalyzing(4, 4).return_truth_table()
#print rn.random_noncanalysing_func(0).return_truth_table()

# def random_nested(num_vars):
#     """Generates a random nested canalyzing function"""
#     initial = random.randint(0, 1)
#     core = random.randint(0, 1)
#     variables = range(num_vars)
#     partitioned = partition.random_partition(variables)
#     desired = [random.randint(0, 1) for _ in range(num_vars)]
#     if len(partitioned) != 1 and len(partitioned[-1]) == 1 and core == 1:
#         return random_nested(num_vars, initial)
# #    if core == 1 and len(partitioned) == 1 and len(partitioned[0]) == 1:
# #    if len(partitioned) == 1 and len(partitioned[0]) == 1:
# #        return random_nested(num_vars)
#     if (initial + len(partitioned) + 1) % 2 == core:
#         return random_nested(num_vars,initial)
#     def evaluator(input_table):
#         """Method for evaluating the function to create a truth table"""
#         start = 0
#         for i, subset in enumerate(partitioned):
#             for j in subset:
#                 if input_table[j] == desired[start]:
#                     return (initial + i) % 2
#                 start += 1
#         return core
#     result = []
#     for i in range(2 ** num_vars):
#         state = [int(j) for j in list(dds.binary_fixed_length(i, num_vars))]
#         result.append(evaluator(state))
#     return dds.Truth(result)

def random_nested(num_vars, initial = None):
    """Generates a random nested canalyzing function with the given initial value"""
    if initial == None:
        initial = random.randint(0, 1)
    core = random.randint(0, 1)
    variables = range(num_vars)
    partitioned = partition.random_partition(variables)
    desired = [random.randint(0, 1) for _ in range(num_vars)]
    if len(partitioned) != 1 and len(partitioned[-1]) == 1 and core == 1:
        return random_nested(num_vars, initial)
#    if core == 1 and len(partitioned) == 1 and len(partitioned[0]) == 1:
#    if len(partitioned) == 1 and len(partitioned[0]) == 1:
#        return random_nested(num_vars)
    if (initial + len(partitioned) + 1) % 2 == core:
        return random_nested(num_vars, initial)
    def evaluator(input_table):
        """Method for evaluating the function to create a truth table"""
        start = 0
        for i, subset in enumerate(partitioned):
            for j in subset:
                if input_table[j] == desired[start]:
                    return (initial + i) % 2
                start += 1
        return core
    result = []
    for i in range(2 ** num_vars):
        state = [int(j) for j in list(dds.binary_fixed_length(i, num_vars))]
        result.append(evaluator(state))
    return dds.Truth(result)
#print random_k_canalyzing(3, 1).return_truth_table()
