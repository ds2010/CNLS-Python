"""
@Title   : Convex Nonparametric Least Square (CNLS)
@Author  : Sheng Dai, Timo Kuosmanen
@Mail    : sheng.dai@aalto.fi (S. Dai); timo.kuosmanen@aalto.fi (T. Kuosmanen)  
@Time    : 2020-04-12 
"""

import numpy as np
import mosek
import cvxopt
from cvxopt import solvers, matrix, spmatrix
solvers.options['show_progress'] = 0

def cnls_crs(x, y, solver):
    
    # Number of the input(s)
    m = np.shape(x)[1]
    
    # Number of the DMUs
    n = len(y)
    
    # Number of the variables 
    nvars = n*(m+1)

    # Define the matrix P
    P = spmatrix(1.0, range(n), range(n), (nvars, nvars))
    
    # define the matrix q
    q = matrix(0.0, (nvars,1))
    q[:n] = -y

    # Define the matrix G
    G = spmatrix([],[],[], (n**2+m*n, nvars))
    I = spmatrix(-1.0, range(n), range(n))

    # FIRST CONSTAINT: Afriat inequalities
    for i in range(n):
    # coefficients of yhat[i]
        G[list(range(i*n, (i+1)*n)), i] = -1.0
        
    # coefficients of yhat[j]    
        G[list(range(i*n, (i+1)*n)), list(range(n))] -= I

    for i in range(n):
        for j in range(m):
    # coefficients of beta[i,j]
            G[list(range(i*n, (i+1)*n)), (j+1)*n+i] = x[i,j] - x[:,j]

    # SECOND CONSTAINT: monotonicity 
    # coefficients of beta 
            G[n**2+i+n*j, (j+1)*n+i] = -1.0  
    
    # Alpha = 0
    # Define the matrix A
    A = spmatrix(-1.0, range(n), range(n), (n, nvars))
    for i in range(n):
        for j in range(m):
        # coefficients of g[i,j] 
             A[i, (j+1)*n+i] = x[i,j]

    # Define the matrix h
    h = matrix(0.0, (n**2+m*n,1))

    # Define the matrix b
    b = matrix(0.0, (n,1))  
        
    if (solver == 'CVXOPT'):
    # default solver 
        sol  = cvxopt.solvers.qp(P, q, G, h, A, b)

    if (solver == 'MOSEK'):
    # Alternative solver
        cvxopt.solvers.options['mosek'] = {mosek.dparam.optimizer_max_time:  100.0, 
                                           mosek.iparam.intpnt_solve_form:   mosek.solveform.dual}

        cvxopt.solvers.options['verbose'] = False

        sol  = cvxopt.solvers.qp(P, q, G, h, A, b, solver='mosek')
    
    # store yhat and g estimates in 'res'
    res = sol['x']

    return res
