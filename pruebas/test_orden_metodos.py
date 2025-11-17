import numpy as np
from metodos.rk2 import rk2
from metodos.rk4 import rk4
from ecuaciones.primer_orden import logistica
from soluciones_analiticas.analiticas import logistica_exacta
from utils.graficador import graficar_comparacion

def test_orden():
    print("=== Prueba de orden de los métodos ===\n")
    t0, P0, tf = 0.0, 0.20, 5.0
    
    pasos = [0.2, 0.1, 0.05, 0.025]
    errores_rk2 = []
    errores_rk4 = []
    
    for h in pasos:
        t_rk2, sol_rk2 = rk2(logistica, t0, P0, h, tf)
        t_rk4, sol_rk4 = rk4(logistica, t0, P0, h, tf)
        
        exact_rk2 = logistica_exacta(t_rk2)
        exact_rk4 = logistica_exacta(t_rk4)
        
        err2 = np.max(np.abs(sol_rk2 - exact_rk2))
        err4 = np.max(np.abs(sol_rk4 - exact_rk4))
        
        errores_rk2.append(err2)
        errores_rk4.append(err4)
    
    print("h      | Error RK2    | Cociente | Error RK4     | Cociente")
    print("-------+--------------+----------+---------------+----------")
    for i in range(1, len(pasos)):
        cociente2 = errores_rk2[i-1] / errores_rk2[i]
        cociente4 = errores_rk4[i-1] / errores_rk4[i]
        print(f"{pasos[i]:.3f}  | {errores_rk2[i]:.2e} | {cociente2:.2f}    | {errores_rk4[i]:.2e}  | {cociente4:.2f}")

if __name__ == "__main__":
    test_orden()