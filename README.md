# GraphOT

This package provides tools to solve primal and dual optimal transport problems on graphs, and to visualize transport flows.

## Usage

```bash 
from src.ot_solver import solver_primal_ot, solver_dual_ot
from src.adj_to_dist import adj_to_dist
from src.visualize import plot_graph_with_potentials, plot_graph_with_transport

# Prepare your data: distributions mu, nu and cost matrix Cost
# ...

P = solver_prime_ot(mu, nu, Cost)
f, g = solve_dual_ot(mu, nu, Cost)

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
