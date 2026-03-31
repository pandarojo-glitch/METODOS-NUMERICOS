import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# =========================
# MÉTODOS NUMÉRICOS
# =========================pyepy
def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_diff(f, x, h):
    return (f(x) - f(x - h)) / h

def central_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2*h)

# =========================
# ERRORES
# =========================
def errores(exacto, aproximado):
    error_abs = np.abs(aproximado - exacto)
    error_rel = error_abs / (np.abs(exacto) + 1e-10)
    error_cuad = error_abs**2
    return error_abs, error_rel, error_cuad

# =========================
# FUNCIÓN GENERAL
# =========================
def resolver_ejercicio(f, df, a, b, h, nombre):
    x = np.arange(a, b + h, h)

    exacta = df(x)
    adelante = forward_diff(f, x, h)
    atras = backward_diff(f, x, h)
    centrada = central_diff(f, x, h)

    # errores
    ea_f, er_f, ec_f = errores(exacta, adelante)
    ea_b, er_b, ec_b = errores(exacta, atras)
    ea_c, er_c, ec_c = errores(exacta, centrada)

    # =========================
    # TABLA
    # =========================
    tabla = pd.DataFrame({
        'x': x,
        'Exacta': exacta,
        'Adelante': adelante,
        'Atrás': atras,
        'Centrada': centrada,
        'Error Abs F': ea_f,
        'Error Abs B': ea_b,
        'Error Abs C': ea_c
    })

    print(f"\n===== {nombre} =====")
    print(tabla.head(10))  # muestra primeras filas

    # =========================
    # GRÁFICAS
    # =========================
    plt.figure()
    plt.plot(x, f(x), label="Función")
    plt.plot(x, exacta, label="Derivada Exacta")
    plt.plot(x, adelante, '--', label="Adelante")
    plt.plot(x, atras, '-.', label="Atrás")
    plt.plot(x, centrada, ':', label="Centrada")
    plt.title(nombre)
    plt.legend()
    plt.grid()
    plt.show()

    # ERRORES
    plt.figure()
    plt.plot(x, ea_f, '--', label="Error Adelante")
    plt.plot(x, ea_b, '-.', label="Error Atrás")
    plt.plot(x, ea_c, ':', label="Error Centrada")
    plt.title(f"Errores - {nombre}")
    plt.legend()
    plt.grid()
    plt.show()

    return tabla


# =========================
# EJERCICIO 1
# f(x) = sin(x)
# =========================
f1 = lambda x: np.sin(x)
df1 = lambda x: np.cos(x)

tabla1 = resolver_ejercicio(f1, df1, 0, np.pi, 0.1, "Ejercicio 1")

# =========================
# EJERCICIO 2
# f(x) = e^x
# =========================
f2 = lambda x: np.exp(x)
df2 = lambda x: np.exp(x)

tabla2 = resolver_ejercicio(f2, df2, 0, 2, 0.05, "Ejercicio 2")

# =========================
# EJERCICIO 3
# f(x) = x^3 - 2x^2 + x
# =========================
f3 = lambda x: x**3 - 2*x**2 + x
df3 = lambda x: 3*x**2 - 4*x + 1

tabla3 = resolver_ejercicio(f3, df3, -1, 2, 0.2, "Ejercicio 3")