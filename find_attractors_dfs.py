"""Find attractors using the other new method discussed at the meeting on 6/3/18"""
import numpy as np
#import pyximport
#pyximport.install()

def dfs(vertex, old_v, graph, visited, basin_size):
    """Standard DFS with a twist that you can't go back in the direction you were just going in"""
    visited[vertex] = 1
    basin_size[0] = basin_size[0] + 1
    old_count = 0
    repeat = -1
    for i in graph[vertex]:
        if i == vertex:
            repeat = i
        elif i == old_v:
            old_count += 1
            if old_count == 2:
                repeat = old_v
        else:
            temp_repeat = dfs(i, vertex, graph, visited, basin_size)
            if temp_repeat != -1:
                repeat = temp_repeat
            if visited[i] == 1:
                repeat = i
    return repeat

def to_state_function(functions):
    """Converts a numpy matrix of functions to a state function"""
    temp = functions.T
    power_vector = np.power(2, np.arange(temp.shape[1] - 1, -1, -1)).T
    return np.dot(temp, power_vector)[0, :].tolist()[0]

def to_graph(state_function):
    """Converts a state function to a graph"""
    graph = []
    length = len(state_function)
    for i in range(length):
        graph.append([])
    for i, val in enumerate(state_function):
        graph[i].append(val)
        graph[val].append(i)
    return graph

def find_attractors_and_basins(functions):
    """Find the attractors and basins of a DDS with f_i = functions[i]
    Input notes:
    functions is a numpy matrix that is just the matrix version of a list of functions
    in list form
    Output notes:
    A list of tuples is output where the first element is the size of the attractor and
    the second the size of the corresponding basin"""
    state_function = to_state_function(functions)
    graph = to_graph(state_function)
    a_and_b_tuples = []
    used = [0] * len(state_function)
    for i in range(len(state_function)):
        if used[i] == 1:
            continue
        visited = [0] * len(state_function)
        visited[i] = 1
        basin_size = [1]#Just so I don't have to deal with returning this value
        point_on_attractor = i
        for j in graph[i]:
            if j != i:
                temp = dfs(j, i, graph, visited, basin_size)
                if temp != -1:
                    point_on_attractor = temp
        attractor_length = 1
        move = state_function[point_on_attractor]
        while move != point_on_attractor:
            move = state_function[move]
            attractor_length += 1
        a_and_b_tuples.append([attractor_length, basin_size[0]])
        for i in range(len(state_function)):
            if visited[i] == 1:
                used[i] = 1
    return a_and_b_tuples
