import numpy as np

def no_homogenea(t, Y):
    """
    Opción A (elegida): y'' - 4y = e^{-t}
    y(0)=1, y'(0)=0
    Sistema:
        y1' = y2
        y2' = 4*y1 + e^{-t}
    """
    y1, y2 = Y
    dy1_dt = y2
    dy2_dt = 4 * y1 + np.exp(-t)
    return np.array([dy1_dt, dy2_dt])