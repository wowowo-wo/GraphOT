# GraphOT

This package provides useful tools to treat optimal transport problems on graphs

## Usage

```bash 
from ssolver import solver_primal_ot, solver_dual_ot
from adj_to_dist import adj_to_dist
from visualize import plot_graph_with_potentials, plot_graph_with_transport

# Prepare your data: adjacency matrix, distributions mu, nu and cost matrix Cost

P = solver_primal_ot(mu, nu, Cost)
f, g = solver_dual_ot(mu, nu, Cost)

print(f"Optimal transport plan (P):\n{P}\n")
print(f"Kantorovich potential f:\n{f}\n")
print(f"Kantorovich potential g:\n{g}\n")

# Plotting example
plot_graph_with_potentials(adj_matrix, f, g)
plot_graph_with_transport(adj_matrix, P)

 ```
 
## Installation

```bash
git clone https://github.com/wowowo-wo/GraphOT
cd GraphOT
pip install .
```
