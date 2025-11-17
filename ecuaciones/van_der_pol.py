import numpy as np

def van_der_pol(t, U, mu=1.0):
    """
    Oscilador de Van der Pol
    x' = y
    y' = μ(1 - x²)y - x
    Parámetro μ = 1 (puedes cambiarlo)
    C.I. típicas: x(0)=2, y(0)=0
    """
    x, y = U
    dx_dt = y
    dy_dt = mu * (1 - x**2) * y - x
    return np.array([dx_dt, dy_dt])