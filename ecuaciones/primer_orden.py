import numpy as np

def logistica(t, P):
    """Ecuación logística: P' = a*P - b*P², a=2, b=1, P(0)=0.20"""
    a, b = 2.0, 1.0
    return a * P - b * P**2

def lineal_primer_orden(t, y):
    """y' + 2t y = t³, y(0)=0"""
    return t**3 - 2*t * y