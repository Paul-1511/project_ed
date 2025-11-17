# main.py
import os
import numpy as np
import matplotlib.pyplot as plt

# Importar métodos
from metodos.rk2 import rk2
from metodos.rk4 import rk4

# Ecuaciones
from ecuaciones.primer_orden import logistica, lineal_primer_orden
from ecuaciones.segundo_orden import no_homogenea  # Opción A elegida
from ecuaciones.sistema_lineal import sistema_lineal
from ecuaciones.van_der_pol import van_der_pol

# Soluciones analíticas
from soluciones_analiticas.analiticas import (
    logistica_exacta,
    lineal_exacta,
    segundo_orden_exacta,
)

# Utilidades
from utils.graficador import graficar_comparacion, graficar_van_der_pol
from utils.comparador import comparar_con_exacta, tabla_convergencia

# Crear carpeta de resultados
os.makedirs("resultados", exist_ok=True)

def main():
    print("PROYECTO FINAL - RK2 y RK4")
    print("Generando resultados para el informe...\n")

    # ===================================================================
    # 1. TABLAS DE CONVERGENCIA (evidencia del orden del método)
    # ===================================================================
    print("1. Generando tablas de convergencia (orden 2 y 4)...")
    tabla_convergencia(logistica, 0.20, 0.0, 4.0, logistica_exacta, "Ecuación Logística")
    tabla_convergencia(lineal_primer_orden, 0.0, 0.0, 3.0, lineal_exacta, "Lineal 1er orden")

    # Para segundo orden (solo comparamos y(t), no y'(t))
    def y_exacta_segundo(t):
        return segundo_orden_exacta(t)

    print("\n2. Comparaciones detalladas con gráficos y CSV...\n")

    # ===================================================================
    # 2. ECUACIÓN LOGÍSTICA
    # ===================================================================
    t, sol = rk2(logistica, 0.0, 0.20, 0.05, 5.0)
    comparar_con_exacta(t, sol, logistica_exacta(t),
                        metodo_nombre="RK2", ecuacion_nombre="Logística", h=0.05, guardar=True)

    t, sol = rk4(logistica, 0.0, 0.20, 0.05, 5.0)
    comparar_con_exacta(t, sol, logistica_exacta(t),
                        metodo_nombre="RK4", ecuacion_nombre="Logística", h=0.05, guardar=True)

    # ===================================================================
    # 3. LINEAL DE PRIMER ORDEN
    # ===================================================================
    t, sol = rk4(lineal_primer_orden, 0.0, 0.0, 0.05, 3.0)
    comparar_con_exacta(t, sol, lineal_exacta(t),
                        metodo_nombre="RK4", ecuacion_nombre="Lineal y' + 2ty = t³", h=0.05, guardar=True)

    # ===================================================================
    # 4. SEGUNDO ORDEN NO HOMOGÉNEA (Opción A elegida)
    # ===================================================================
    t, sol = rk4(no_homogenea, 0.0, np.array([1.0, 0.0]), 0.02, 5.0)
    y_numerica = sol[:, 0]  # solo comparamos y(t)
    comparar_con_exacta(t, y_numerica, segundo_orden_exacta(t),
                        metodo_nombre="RK4", ecuacion_nombre="y'' - 4y = e^{-t}", h=0.02, guardar=True)

    # ===================================================================
    # 5. SISTEMA LINEAL 2×2 (solo el Sistema 1, como quedó aprobado)
    # ===================================================================
    t, sol = rk4(sistema_lineal, 0.0, np.array([1.0, 0.0]), 0.01, 10.0)
    plt.figure(figsize=(8, 6))
    plt.plot(sol[:, 0], sol[:, 1], 'b-', linewidth=2)
    plt.title("Sistema lineal 2×2 - Trayectoria en plano fase\nx' = -x + 2y, y' = -3x - 4y")
    plt.xlabel("x(t)"); plt.ylabel("y(t)"); plt.grid(True)
    plt.savefig("resultados/sistema_lineal_plano_fase.png", dpi=300, bbox_inches='tight')
    plt.show()

    # ===================================================================
    # 6. VAN DER POL (mu = 1) → Caso final sin solución analítica
    # ===================================================================
    print("\n6. Resolviendo Oscilador de Van der Pol (mu = 1)...")
    t, sol = rk4(van_der_pol, 0.0, np.array([2.0, 0.0]), 0.02, 40.0, 1.0)  # Pasar mu como argumento posicional
    graficar_van_der_pol(t, sol, "Oscilador de Van der Pol (mu=1) - RK4")

    # Guardar datos del Van der Pol
    np.savetxt("resultados/van_der_pol_mu1.csv",
               np.column_stack([t, sol]),
               delimiter=",", header="t,x,y", comments="")

    print("\n¡TODO COMPLETADO!")
    print("Archivos generados en la carpeta 'resultados/':")
    print("   → CSVs con datos numéricos")
    print("   → Gráficos comparativos y de fase")
    print("   → Tablas de convergencia en consola (copia-pega al informe)")
    print("\n¡Listo para comprimir y entregar!")

if __name__ == "__main__":
    main()