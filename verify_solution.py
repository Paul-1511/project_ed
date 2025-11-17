#!/usr/bin/env python
import matplotlib
matplotlib.use('Agg')

import numpy as np
from metodos.rk4 import rk4
from ecuaciones.primer_orden import lineal_primer_orden
from soluciones_analiticas.analiticas import lineal_exacta

# Verificar la ecuación lineal
t_rk4, sol_rk4 = rk4(lineal_primer_orden, 0.0, 0.0, 0.05, 3.0)
exact = lineal_exacta(t_rk4)

print("\nVerificación de la solución lineal de primer orden:")
print(f"Error máximo: {np.max(np.abs(sol_rk4 - exact)):.2e}")
print(f"Error medio: {np.mean(np.abs(sol_rk4 - exact)):.2e}")

# Mostrar algunos valores
print("\nPrimeros valores:")
for i in range(min(5, len(t_rk4))):
    print(f"  t={t_rk4[i]:.2f}: RK4={sol_rk4[i]:.6f}, Exacta={exact[i]:.6f}, Error={abs(sol_rk4[i]-exact[i]):.2e}")
