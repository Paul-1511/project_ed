# Project ED - Métodos Numéricos para Ecuaciones Diferenciales

Proyecto de implementación y comparación de métodos numéricos (Runge-Kutta de orden 2 y 4) para resolver ecuaciones diferenciales ordinarias.

## 📋 Descripción

Este proyecto implementa métodos numéricos para resolver:

- **Ecuaciones de primer orden:**
  - Logística: $y' = y(1-y)$
  - Lineal: $y' + 2ty = t^3$, con $y(0) = 0$

- **Ecuaciones de segundo orden:**
  - No homogénea: $y'' - 4y = e^{-t}$, con $y(0) = 1$, $y'(0) = 0$

- **Sistemas de ecuaciones:**
  - Sistema lineal 2×2
  - Oscilador de Van der Pol: $y'' - \mu(1-y^2)y' + y = 0$

## 🔧 Métodos Implementados

- **RK2 (Heun):** Método de Runge-Kutta de orden 2
- **RK4:** Método de Runge-Kutta de orden 4

## 📁 Estructura del Proyecto

```
project_ed/
├── main.py                      # Script principal
├── run_main.py                  # Ejecutor con configuración de matplotlib
├── README.md                    # Este archivo
├── .gitignore                   # Archivos ignorados por git
├── ecuaciones/                  # Definiciones de ecuaciones diferenciales
│   ├── __init__.py
│   ├── primer_orden.py         # EDOs de primer orden
│   ├── segundo_orden.py        # EDOs de segundo orden
│   ├── sistema_lineal.py       # Sistema lineal 2×2
│   └── van_der_pol.py          # Oscilador de Van der Pol
├── metodos/                    # Métodos numéricos
│   ├── __init__.py
│   ├── rk2.py                  # Runge-Kutta orden 2
│   └── rk4.py                  # Runge-Kutta orden 4
├── soluciones_analiticas/      # Soluciones exactas
│   ├── __init__.py
│   └── analiticas.py           # Fórmulas analíticas para comparación
├── utils/                      # Utilidades
│   ├── __init__.py
│   ├── comparador.py           # Análisis de convergencia
│   └── graficador.py           # Visualización de resultados
└── pruebas/                    # Scripts de prueba
    └── test_orden_metodos.py   # Verificación de convergencia
```

## 🚀 Instalación

### Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Paul-1511/project_ed.git
   cd project_ed
   ```

2. **Crear un entorno virtual (recomendado):**
   ```bash
   python -m venv .venv
   ```

3. **Activar el entorno virtual:**

   - **En Windows (PowerShell):**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   
   - **En Windows (CMD):**
     ```cmd
     .venv\Scripts\activate.bat
     ```
   
   - **En Linux/macOS:**
     ```bash
     source .venv/bin/activate
     ```

4. **Instalar dependencias:**
   ```bash
   pip install numpy matplotlib
   ```

## 📊 Uso

### Ejecutar el Programa Principal

```bash
python run_main.py
```

O alternativamente:
```bash
python main.py
```

Este script ejecutará:
- Resolución de la ecuación logística con RK2 y RK4
- Resolución de la ecuación lineal de primer orden
- Resolución de la ecuación de segundo orden
- Resolución del sistema lineal 2×2 (gráfico en el plano fase)
- Resolución del oscilador de Van der Pol
- Análisis de convergencia y orden de los métodos

### Archivos de Salida

Se generarán archivos CSV con los resultados:
- `resultados/Logistica_RK2_h0.05.csv`
- `resultados/Logistica_RK4_h0.05.csv`
- `resultados/Lineal_y'_+_2ty_=_t³_RK4_h0.05.csv`
- `resultados/y''_-_4y_=_e^{-t}_RK4_h0.02.csv`
- `resultados/sistema_lineal_plano_fase.png`

### Verificar las Soluciones Analíticas

Para verificar la exactitud de las soluciones:
```bash
python verify_solution.py      # Verifica solución de primer orden
python verify_segundo.py       # Verifica solución de segundo orden
```

## 📈 Resultados Esperados

### Convergencia de Métodos

- **RK2:** Orden de convergencia ≈ 2
- **RK4:** Orden de convergencia ≈ 4

### Errores Numéricos

- **Ecuación lineal:** Error máximo < 1e-5
- **Ecuación de segundo orden:** Error máximo < 1e-3

### Gráficos Generados

- Soluciones numéricas vs analíticas
- Análisis de error absoluto
- Plano de fase del sistema lineal
- Trayectorias del oscilador de Van der Pol

## 🔍 Detalles de Implementación

### Ecuación Lineal: $y' + 2ty = t^3$

**Solución Analítica:**
$$y(t) = \frac{1}{2}[t^2 - 1 + e^{-t^2}]$$

**Condición Inicial:** $y(0) = 0$

### Ecuación de Segundo Orden: $y'' - 4y = e^{-t}$

**Solución Analítica:**
$$y(t) = \frac{7}{12}e^{2t} + \frac{3}{4}e^{-2t} - \frac{1}{3}e^{-t}$$

**Condiciones Iniciales:** $y(0) = 1$, $y'(0) = 0$

### Oscilador de Van der Pol

Parámetro: $\mu = 1.0$

Sistema de ecuaciones de primer orden:
- $y_1' = y_2$
- $y_2' = \mu(1 - y_1^2)y_2 - y_1$

## 📝 Notas Técnicas

- El proyecto usa `matplotlib` con backend `Agg` para compatibilidad en sistemas Windows
- Se emplean caracteres ASCII en salida de consola para evitar problemas de codificación
- Los archivos CSV contienen: tiempo, solución numérica, solución analítica (si aplica), error absoluto

## 👤 Autor

Paul-1511

## 📄 Licencia

Este proyecto se proporciona con fines educativos.

## 📞 Soporte

Para reportar errores o sugerir mejoras, abra un issue en el repositorio.
