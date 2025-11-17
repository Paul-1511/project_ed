import numpy as np

def rk4(f, t0, y0, h, tf, *args):
    t_vals = np.arange(t0, tf + h, h)
    n = len(t_vals)
    
    if np.isscalar(y0):
        y_vals = np.zeros(n)
        y_vals[0] = y0
        for i in range(n-1):
            t, y = t_vals[i], y_vals[i]
            k1 = f(t, y, *args)
            k2 = f(t + h/2, y + h/2 * k1, *args)
            k3 = f(t + h/2, y + h/2 * k2, *args)
            k4 = f(t + h, y + h * k3, *args)
            y_vals[i+1] = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    else:
        m = len(y0)
        y_vals = np.zeros((n, m))
        y_vals[0] = y0
        for i in range(n-1):
            t, y = t_vals[i], y_vals[i]
            k1 = f(t, y, *args)
            k2 = f(t + h/2, y + h/2 * k1, *args)
            k3 = f(t + h/2, y + h/2 * k2, *args)
            k4 = f(t + h, y + h * k3, *args)
            y_vals[i+1] = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    
    return t_vals, y_vals