import numpy as np

def logistica_exacta(t, P0=0.20, a=2.0, b=1.0):
    """Solución analítica de la logística"""
    return (a * P0 * np.exp(a * t)) / (a + P0 * (np.exp(a * t) - 1) * b)

def lineal_exacta(t):
    """Solución analítica de y' + 2ty = t³, y(0)=0
    Factor integrante: e^(t²)
    Solución: y = (1/2)[t² - 1 + e^(-t²)]"""
    return (1/2) * (t**2 - 1 + np.exp(-t**2))

def segundo_orden_exacta(t):
    """Solución exacta de y'' - 4y = e^{-t}, y(0)=1, y'(0)=0
    y = (7/12)*e^{2t} + (3/4)*e^{-2t} - (1/3)*e^{-t}"""
    return (7/12)*np.exp(2*t) + (3/4)*np.exp(-2*t) - (1/3)*np.exp(-t)