import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# =========================
# REGLA DEL TRAPECIO
# =========================
def trapecio(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    integral = (h/2) * (y[0] + 2*np.sum(y[1:n]) + y[n])
    return integral, x, y

# =========================
# ERROR
# =========================
def error(exacto, aproximado):
    return abs(exacto - aproximado)

# =========================
# EJERCICIO 1
# ∫(x² + 3x + 1) dx de 0 a 2
# =========================
def ejercicio1():
    f = lambda x: x**2 + 3*x + 1
    a, b = 0, 2

    # solución exacta
    exacto = (2**3)/3 + (3*(2**2))/2 + 2

    n_values = [10, 20, 50]
    resultados = []

    for n in n_values:
        aprox, _, _ = trapecio(f, a, b, n)
        err = error(exacto, aprox)
        resultados.append([n, aprox, err])

    tabla = pd.DataFrame(resultados, columns=["n", "Aproximación", "Error"])
    print("\nEjercicio 1")
    print(tabla)

# =========================
# EJERCICIO 2
# ∫ e^(-x^2) dx de 1 a 4
# =========================
def ejercicio2():
    f = lambda x: np.exp(-x**2)
    a, b = 1, 4

    n_values = [5, 10, 15]
    resultados = []

    for n in n_values:
        aprox, _, _ = trapecio(f, a, b, n)
        resultados.append([n, aprox])

    tabla = pd.DataFrame(resultados, columns=["n", "Aproximación"])
    print("\nEjercicio 2")
    print(tabla)

# =========================
# EJERCICIO 3
# ∫ sin(x) dx de 0 a pi
# =========================
def ejercicio3():
    f = lambda x: np.sin(x)
    a, b = 0, np.pi
    exacto = 2

    n_values = [5, 10, 20, 50]
    resultados = []

    for n in n_values:
        aprox, x, y = trapecio(f, a, b, n)
        err = error(exacto, aprox)
        resultados.append([n, aprox, err])

        # gráfica
        x_fine = np.linspace(a, b, 100)
        plt.figure()
        plt.plot(x_fine, f(x_fine), label="f(x)")
        plt.fill_between(x, y, alpha=0.3, label=f"n={n}")
        plt.title(f"Aproximación Trapecio (n={n})")
        plt.legend()
        plt.grid()
        plt.show()

    tabla = pd.DataFrame(resultados, columns=["n", "Aproximación", "Error"])
    print("\nEjercicio 3")
    print(tabla)

# =========================
# MAIN
# =========================
ejercicio1()
ejercicio2()
ejercicio3()