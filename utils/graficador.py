import matplotlib.pyplot as plt
import numpy as np

def graficar_comparacion(t, y_num, y_exact, titulo="", metodo=""):
    plt.figure(figsize=(10, 6))
    plt.plot(t, y_num, 'b-', label=f'{metodo} (numérico)')
    plt.plot(t, y_exact, 'r--', label='Solución exacta')
    plt.title(f"{titulo}\nMétodo: {metodo}")
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.legend()
    plt.grid(True)
    plt.show()

def graficar_fases(x, y, titulo="", metodo=""):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'b-')
    plt.title(f"Plano fase - {titulo}\nMétodo: {metodo}")
    plt.xlabel('x(t)')
    plt.ylabel('y(t)')
    plt.grid(True)
    plt.show()

def graficar_van_der_pol(t, sol, titulo="Oscilador de Van der Pol"):
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(t, sol[:, 0], label='x(t)')
    plt.plot(t, sol[:, 1], label='y(t)')
    plt.title(f"{titulo} - Series temporales")
    plt.legend(); plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(sol[:, 0], sol[:, 1])
    plt.title("Plano fase (ciclo límite)")
    plt.xlabel('x'); plt.ylabel('y')
    plt.grid(True)
    plt.tight_layout()
    plt.show()