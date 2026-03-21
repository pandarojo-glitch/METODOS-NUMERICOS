import numpy as np
import matplotlib.pyplot as plt
import csv

def gauss_seidel(A, b, tol=1e-6, max_iter=100):
    if A.shape[0] != A.shape[1]:
        raise ValueError("La matriz A debe ser cuadrada")

    n = len(b)
    x = np.zeros(n)
    x_prev = np.copy(x)

    errors = []

    for k in range(max_iter):
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x_prev[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]

        abs_error = np.linalg.norm(x - x_prev, ord=np.inf)
        rel_error = abs_error / (np.linalg.norm(x, ord=np.inf) + 1e-10)
        quad_error = np.linalg.norm(x - x_prev) ** 2

        errors.append((k, abs_error, rel_error, quad_error))

        if abs_error < tol:
            break

        x_prev = np.copy(x)

    return x, errors


# -----------------------------
# EJERCICIO 1
# -----------------------------
A1 = np.array([
    [10, 2, 3, 1],
    [2, 12, 2, 3],
    [3, 2, 15, 1],
    [1, 3, 1, 10]
], dtype=float)

b1 = np.array([15, 22, 18, 10], dtype=float)


# -----------------------------
# EJERCICIO 2 (5x5 corregido)
# -----------------------------
A2 = np.array([
    [20, -5, -3, 0, 0],
    [-4, 18, -2, -1, 0],
    [-3, -1, 22, -5, 0],
    [0, -2, -4, 25, -1],
    [0, 0, 0, 0, 1]
], dtype=float)

b2 = np.array([100, 120, 130, 150, 0], dtype=float)


# -----------------------------
# EJERCICIO 3 (10x10 corregido)
# -----------------------------
A3 = np.zeros((10,10))

A3[0,0]=15; A3[0,1]=-4; A3[0,2]=-1; A3[0,3]=-2
A3[1,0]=-3; A3[1,1]=18; A3[1,2]=-2; A3[1,4]=-1
A3[2,0]=-1; A3[2,1]=-2; A3[2,2]=20; A3[2,5]=-5
A3[3,0]=-2; A3[3,1]=-1; A3[3,2]=-4; A3[3,3]=22; A3[3,6]=-1
A3[4,1]=-1; A3[4,2]=-3; A3[4,3]=-1; A3[4,4]=25; A3[4,7]=-2
A3[5,2]=-2; A3[5,4]=-1; A3[5,5]=28; A3[5,8]=-1
A3[6,3]=-4; A3[6,5]=-2; A3[6,6]=30; A3[6,9]=-3
A3[7,4]=-1; A3[7,6]=-1; A3[7,7]=35; A3[7,8]=-2
A3[8,5]=-2; A3[8,7]=-3; A3[8,8]=40; A3[8,9]=-1
A3[9,6]=-3; A3[9,8]=-1; A3[9,9]=45

b3 = np.array([200,250,180,300,270,310,320,400,450,500], dtype=float)


# -----------------------------
# RESOLVER
# -----------------------------
x1, e1 = gauss_seidel(A1, b1)
x2, e2 = gauss_seidel(A2, b2)
x3, e3 = gauss_seidel(A3, b3)

print("Solución Ejercicio 1:", x1)
print("Solución Ejercicio 2:", x2)
print("Solución Ejercicio 3:", x3)


# -----------------------------
# GUARDAR CSV
# -----------------------------
with open("errores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Sistema", "Iter", "Error abs", "Error rel", "Error cuad"])

    for e in e1:
        writer.writerow(["E1"] + list(e))
    for e in e2:
        writer.writerow(["E2"] + list(e))
    for e in e3:
        writer.writerow(["E3"] + list(e))


# -----------------------------
# FUNCIÓN PARA GRAFICAR
# -----------------------------
def graficar_errores(errors, titulo, archivo):
    iteraciones = [e[0] for e in errors]
    abs_error = [e[1] for e in errors]
    rel_error = [e[2] for e in errors]
    quad_error = [e[3] for e in errors]

    plt.figure()
    plt.plot(iteraciones, abs_error, label="Error absoluto")
    plt.plot(iteraciones, rel_error, label="Error relativo")
    plt.plot(iteraciones, quad_error, label="Error cuadrático")

    plt.yscale("log")
    plt.xlabel("Iteraciones")
    plt.ylabel("Error")
    plt.title(titulo)
    plt.legend()
    plt.grid()

    plt.savefig(archivo)
    plt.show()


# -----------------------------
# GENERAR 3 GRÁFICAS
# -----------------------------
graficar_errores(e1, "Convergencia Ejercicio 1", "ejercicio1.png")
graficar_errores(e2, "Convergencia Ejercicio 2", "ejercicio2.png")
graficar_errores(e3, "Convergencia Ejercicio 3", "ejercicio3.png")