# Convex Nonparametric Least Squares (`CNLS`): An alternative formulation

Along with the development of the [StoNED-Python](https://github.com/ds2010/StoNED-Python) project, we recognize that we can reformulate the CNLS estimator and use the Python package, e.g., [CVXOPT](https://cvxopt.org/) to solve it. More discussions can be seen from [CNLS-reformulation](https://github.com/ds2010/AltCNLS-Python/blob/master/CNLS-reformulation.ipynb). Thus, this project provides some basic functions (e.g., [CNLS_CRS](https://github.com/ds2010/AltCNLS-Python/blob/master/Python/CNLS_CRS.py) and [CNLS_VRS](https://github.com/ds2010/AltCNLS-Python/blob/master/Python/CNLS_VRS.py)) and a [tutorial](https://github.com/ds2010/AltCNLS-Python/blob/master/CNLS-VRS.ipynb) to help users recode the CNLS in Python. 

Please note that the `CNLS-Python` can only be applied in the applications of additive error term. For most applications in multiplicative one or other StoNED-related models, please go to our ongoing project [StoNED-Python](https://github.com/ds2010/StoNED-Python).


# Authors:
  
  + [Sheng Dai](https://www.researchgate.net/profile/Sheng_Dai8), Ph.D. candidate, Aalto University School of Business.
  + [Timo Kuosmanen](https://people.aalto.fi/timo.kuosmanen), Professor, Aalto University School of Business.
