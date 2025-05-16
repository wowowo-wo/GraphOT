'''
adj_to_dist:
converts an adjacency matrix to a distance matrix as a NumPy array.  For disconnected graphs, unreachable nodes have distances set to infinity
'''

import numpy as np
from collections import deque

def adj_to_dist(adj_matrix):

    n = len(adj_matrix)
    distance_matrix = np.full((n, n), np.inf)

    for start in range(n):
        queue = deque([start])
        distances = [-1] * n
        distances[start] = 0

        while queue:
            current = queue.popleft()
            for neighbor in range(n):
                if adj_matrix[current][neighbor] == 1 and distances[neighbor] == -1:
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)

        for end in range(n):
            if distances[end] != -1:
                distance_matrix[start][end] = distances[end]

    return distance_matrix