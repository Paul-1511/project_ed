# utils/comparador.py
import numpy as np
import matplotlib.pyplot as plt
import os
from .graficador import graficar_comparacion

def comparar_con_exacta(t, y_num, y_exact, metodo_nombre, ecuacion_nombre, h, guardar=False):
    """
    Compara solución numérica con exacta y genera:
    - Gráfica comparativa
    - Tabla de errores (absoluto y relativo)
    - Métricas: error máximo y medio
    """
    y_num = np.array(y_num).flatten()
    y_exact = np.array(y_exact).flatten()
    
    error_abs = np.abs(y_exact - y_num)
    error_rel = error_abs / (np.abs(y_exact) + 1e-12)
    
    error_max = np.max(error_abs)
    error_medio = np.mean(error_abs)
    error_rel_max = np.max(error_rel)
    
    print(f"\n{'='*60}")
    print(f" RESULTADOS: {ecuacion_nombre}")
    print(f" Método: {metodo_nombre} | h = {h}")
    print(f"{'='*60}")
    print(f" Error absoluto máximo : {error_max:.2e}")
    print(f" Error absoluto medio  : {error_medio:.2e}")
    print(f" Error relativo máximo : {error_rel_max:.2e}")
    print(f" Puntos calculados     : {len(t)}")
    print(f"{'='*60}\n")
    
    # Gráfica
    titulo = f"{ecuacion_nombre}\nh = {h} | Método: {metodo_nombre}"
    graficar_comparacion(t, y_num, y_exact, titulo, metodo_nombre)
    
    # Guardar datos (útil para informe)
    if guardar:
        os.makedirs("resultados", exist_ok=True)
        nombre_archivo = f"resultados/{ecuacion_nombre.replace(' ', '_')}_{metodo_nombre}_h{h}.csv"
        np.savetxt(nombre_archivo,
                   np.column_stack([t, y_num, y_exact, error_abs]),
                   delimiter=",",
                   header="t,y_numerica,y_exacta,error_absoluto",
                   comments="")
        print(f"Datos guardados en: {nombre_archivo}\n")

    return {
        "h": h,
        "error_max": error_max,
        "error_medio": error_medio,
        "metodo": metodo_nombre
    }

def tabla_convergencia(ecuacion_func, y0, t0, tf, solucion_exacta_func, nombre_ecuacion):
    """
    Genera tabla de convergencia para RK2 y RK4 mostrando el orden experimental
    """
    print(f"\nTABLA DE CONVERGENCIA - {nombre_ecuacion}")
    print("-" * 80)
    print(f"{'h':>8} {'RK2 Error máx':>15} {'Cociente':>10} {'RK4 Error máx':>15} {'Cociente':>10}")
    print("-" * 80)
    
    hs = [0.2, 0.1, 0.05, 0.025, 0.0125]
    errores_rk2 = []
    errores_rk4 = []
    
    from metodos.rk2 import rk2
    from metodos.rk4 import rk4
    
    for h in hs:
        t2, sol2 = rk2(ecuacion_func, t0, y0, h, tf)
        t4, sol4 = rk4(ecuacion_func, t0, y0, h, tf)
        
        exact2 = solucion_exacta_func(t2)
        exact4 = solucion_exacta_func(t4)
        
        e2 = np.max(np.abs(sol2 - exact2))
        e4 = np.max(np.abs(sol4 - exact4))
        
        errores_rk2.append(e2)
        errores_rk4.append(e4)
    
    # Imprimir tabla con cocientes
    for i in range(len(hs)):
        c2 = errores_rk2[i-1] / errores_rk2[i] if i > 0 else "-"
        c4 = errores_rk4[i-1] / errores_rk4[i] if i > 0 else "-"
        print(f"{hs[i]:8.4f} {errores_rk2[i]:15.2e} {c2:>10} {errores_rk4[i]:15.2e} {c4:>10}")
    
    print("-" * 80)
    print("Cocientes ~2 -> RK2 (orden 2) | Cocientes ~4 -> RK4 (orden 4)\n")