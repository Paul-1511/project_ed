#!/usr/bin/env python
import matplotlib
matplotlib.use('Agg')

import numpy as np
from metodos.rk4 import rk4
from ecuaciones.segundo_orden import no_homogenea
from soluciones_analiticas.analiticas import segundo_orden_exacta

# y'' - 4y = e^{-t}, y(0)=1, y'(0)=0
# Sistema:
#   y1' = y2
#   y2' = 4*y1 + e^{-t}

t_rk4, sol_rk4 = rk4(no_homogenea, 0.0, np.array([1.0, 0.0]), 0.02, 5.0)
y_numerica = sol_rk4[:, 0]  # Solo comparamos y(t)
exact = segundo_orden_exacta(t_rk4)

print("Verificación de la solución de segundo orden no homogénea:")
print(f"Error máximo: {np.max(np.abs(y_numerica - exact)):.2e}")
print(f"Error medio: {np.mean(np.abs(y_numerica - exact)):.2e}")

# Mostrar algunos valores
print("\nPrimeros valores:")
for i in range(min(5, len(t_rk4))):
    print(f"  t={t_rk4[i]:.2f}: RK4={y_numerica[i]:.6f}, Exacta={exact[i]:.6f}, Error={abs(y_numerica[i]-exact[i]):.2e}")

print("\nÚltimos valores:")
for i in range(max(0, len(t_rk4)-5), len(t_rk4)):
    print(f"  t={t_rk4[i]:.2f}: RK4={y_numerica[i]:.6f}, Exacta={exact[i]:.6f}, Error={abs(y_numerica[i]-exact[i]):.2e}")

# Verificar C.I.
print(f"\nC.I. y(0)={y_numerica[0]:.6f} (debe ser 1.0)")
print(f"C.I. y'(0)={sol_rk4[0, 1]:.6f} (debe ser 0.0)")
