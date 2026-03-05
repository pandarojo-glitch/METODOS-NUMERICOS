import numpy as np
def gauss_elimination(A, b):
    """
    Resuelve el sistema Ax = b usando eliminación gaussiana
    con pivoteo parcial.
    """

    # Copiamos matrices para no modificar las originales
    A = A.copy()
    b = b.copy()

    n = len(b)

    # ===============================
    # ELIMINACIÓN HACIA ADELANTE
    # ===============================
    for i in range(n):

        # ---------------------------
        # PIVOTEO PARCIAL
        # ---------------------------
        # Busca el mayor valor absoluto en la columna actual
        max_row = i + np.argmax(np.abs(A[i:, i]))

        # Intercambia filas si es necesario
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]

        # ---------------------------
        # HACER CEROS DEBAJO DEL PIVOTE
        # ---------------------------
        for j in range(i + 1, n):
            if A[i][i] == 0:
                raise ValueError("El sistema no tiene solución única.")

            factor = A[j][i] / A[i][i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # ===============================
    # SUSTITUCIÓN REGRESIVA
    # ===============================
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        if A[i][i] == 0:
            raise ValueError("División entre cero detectada.")

        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i][i]

    return x
# -----------------------------
# EJERCICIO 1 (4x4)
# -----------------------------
A1 = np.array([
    [3, 2, -1, 4],
    [5, -3, 2, -1],
    [-1, 4, -2, 3],
    [2, -1, 3, 5]
], dtype=float)
b1 = np.array([10, 5, -3, 8], dtype=float)
sol1 = gauss_elimination(A1, b1)
print("Solución Ejercicio 1:")
print(sol1)
print("-" * 50)
# -----------------------------
# EJERCICIO 2 (5x5)
# -----------------------------
A2 = np.array([
    [6, -2, 3, -1, 2],
    [-3, 5, -2, 4, -1],
    [4, 3, 7, -5, 3],
    [-2, 6, -3, 1, -4],
    [1, -3, 2, -5, 6]
], dtype=float)
b2 = np.array([15, -6, 20, -4, 7], dtype=float)
sol2 = gauss_elimination(A2, b2)
print("Solución Ejercicio 2:")
print(sol2)
print("-" * 50)
# -----------------------------
# EJERCICIO 3 (6x6)
# -----------------------------
A3 = np.array([
    [1, 2, -3, 4, -1, 1],
    [-2, 3, 5, -1, 2, -1],
    [4, -1, 2, 6, -3, 1],
    [-3, 5, -1, 2, 4, -1],
    [2, -4, 6, -5, 1, 3],
    [-5, 1, 4, -1, 2, -6]
], dtype=float)

b3 = np.array([7, -2, 10, 3, -8, 5], dtype=float)
sol3 = gauss_elimination(A3, b3)
print("Solución Ejercicio 3:")
print(sol3)
print("-" * 50)
# ==========================================================
# FUNCIÓN PARA QUE EL USUARIO INGRESE SU PROPIA MATRIZ
# ==========================================================
def ingresar_sistema():
    """
    Permite al usuario ingresar manualmente un sistema de ecuaciones.
    """

    n = int(input("¿Cuántas ecuaciones (n x n) tendrá el sistema? "))

    A = np.zeros((n, n))
    b = np.zeros(n)

    print("\nIngrese los coeficientes fila por fila:")

    for i in range(n):
        print(f"\nEcuación {i+1}")
        for j in range(n):
            A[i][j] = float(input(f"Coeficiente A[{i+1}][{j+1}]: "))
        b[i] = float(input("Término independiente: "))
    return A, b
# ==========================================================
# OPCIÓN INTERACTIVA
# ==========================================================
opcion = input("\n¿Desea ingresar su propio sistema? (s/n): ")
if opcion.lower() == 's':
    A_user, b_user = ingresar_sistema()
    solucion_usuario = gauss_elimination(A_user, b_user)
    print("\nSolución del sistema ingresado:")
    print(solucion_usuario)