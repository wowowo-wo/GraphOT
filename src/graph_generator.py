'''
These functions generate various graph adjacency matrices as Numpy array.
'''

import numpy as np

def gen_complete_adj_matrix(n):
    adj_matrix = np.ones((n, n), dtype=int) - np.eye(n, dtype=int)
    return adj_matrix

def gen_cycle_adj_matrix(n):
    adj_matrix = np.zeros((n, n), dtype=int)

    for i in range(n):
        adj_matrix[i, (i+1)%n] = 1
        adj_matrix[i, (i-1)%n] = 1

    return adj_matrix

def gen_path_adj_matrix(n):
    adj_matrix = np.zeros((n, n), dtype=int)

    for i in range(n-1):
        adj_matrix[i, i+1] = 1
        adj_matrix[i+1, i] = 1

    return adj_matrix

def gen_random_adj_matrix(n, edge_prob=0.5, seed=None):

    if seed is not None:
        np.random.seed(seed)

    upper_tri = np.triu(np.random.rand(n, n) < edge_prob, k=1).astype(int)
    adj_matrix = upper_tri + upper_tri.T

    return adj_matrix