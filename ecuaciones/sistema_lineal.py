import numpy as np

def sistema_lineal(t, U):
    """
    x' = -x + 2y
    y' = -3x - 4y
    C.I.: x(0)=1, y(0)=0
    """
    x, y = U
    dx_dt = -x + 2*y
    dy_dt = -3*x - 4*y
    return np.array([dx_dt, dy_dt])