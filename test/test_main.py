import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from graph_generator import gen_random_adj_matrix
from adj_to_dist import adj_to_dist
from solver import solver_primal_ot, solver_dual_ot
from visualize import plot_graph_with_transport, plot_graph_with_potentials

import numpy as np

adj = gen_random_adj_matrix(7,0.6)
C = adj_to_dist(adj) ** 2

a = np.array([0.6, 0.2, 0.0, 0.0, 0.0 , 0.0 , 0.2])
b = np.array([0.0, 0.0, 0.0, 0.4, 0.4 , 0.1 , 0.1])

P = solver_primal_ot(a, b, C)
f, g = solver_dual_ot(a, b, C)

print("Optimal transport plan (P):\n",P,"\n")
print("Kantorovich potential f:\n", f,"\n")
print("Kantorovich potential g:\n", g,"\n")

plot_graph_with_transport(adj, P)

plot_graph_with_potentials(adj,f,g)