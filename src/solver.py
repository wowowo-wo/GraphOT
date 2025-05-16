'''
solver_primal_ot:
Takes two distributions (mu and nu) and cost matrix Cost,then solve the ptimal optimal transport problem using linear programming. Returns the optimal transport plan as an NumPy array.

solver_dual_ot:
Takes two distributions (mu and nu) and cost matrix Cost,then solve the dual optimal transport problem using linear programming. Returns the Kantorovich potentials f and g as NumPy arrays.
'''
import numpy as np
from scipy.optimize import linprog

def solver_primal_ot(mu,nu,Cost):

    if np.isinf(Cost).any():
        raise ValueError("Cost matrix contains infinity values, which is not allowed.")
    
    n = Cost.shape[0]
    c = Cost.flatten()
    A_eq = []
    b_eq = []
    for i in range(n):
        row = np.zeros(n*n)
        row[i*n:(i+1)*n] = 1
        A_eq.append(row)
        b_eq.append(mu[i])
    for j in range(n):
        col = np.zeros(n*n)
        col[j::n] = 1
        A_eq.append(col)
        b_eq.append(nu[j])
    A_eq = np.array(A_eq)
    b_eq = np.array(b_eq)
    bounds = [(0, None) for _ in range(n * n)]
    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    if not result.success:
        raise ValueError("Optimal transport did not converge")
    return result.x.reshape((n, n))

def solver_dual_ot(mu,nu,Cost):

    if np.isinf(Cost).any():
        raise ValueError("Cost matrix contains infinity values, which is not allowed.")
    
    n = Cost.shape[0]
    A_ub = []
    b_ub = []
    for i in range(n):
        for j in range(n):
            constraint = np.zeros(2 * n)
            constraint[i] = 1 
            constraint[n + j] = 1 
            A_ub.append(constraint)
            b_ub.append(Cost[i, j])
    A_ub = np.array(A_ub)
    b_ub = np.array(b_ub)
    c = -np.concatenate([mu, nu]) 
    bounds = [(None, None)] * (2 * n)
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    if not result.success:
        raise ValueError("Optimal transport did not converge")
    f = result.x[:n]
    g = result.x[n:]
    return f, g