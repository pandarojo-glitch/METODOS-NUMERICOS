import numpy as np

def gauss_jordan_pivot_determinante(A, b):
    n = len(A)

    Ab = np.hstack([A, b.reshape(-1, 1)]).astype(float)

    det_A = np.linalg.det(A)

    if np.isclose(det_A, 0):
        print(f"Determinante de A: {det_A:.5f}")
        print("El sistema es indeterminado o no tiene solución única.")
        return None

    print(f"Determinante de A: {det_A:.5f}")
    print("El sistema tiene solución única.")

    for i in range(n):

        max_row = np.argmax(abs(Ab[i:, i])) + i
        if i != max_row:
            Ab[[i, max_row]] = Ab[[max_row, i]]

        Ab[i] = Ab[i] / Ab[i, i]

        for j in range(n):
            if i != j:
                Ab[j] -= Ab[j, i] * Ab[i]

    x = Ab[:, -1]
    return x


# -------------------------
# EJERCICIO 1 (8x8)
# -------------------------

A1 = np.array([
[2,3,-1,4,-2,5,-3,1],
[-3,2,4,-1,3,-2,5,-1],
[4,-1,3,2,-3,1,-2,5],
[-1,5,-2,3,4,-1,2,-3],
[3,-2,5,-1,4,2,-3,1],
[-2,4,-3,1,5,-1,2,-4],
[5,-1,2,-3,4,1,-2,3],
[1,-3,4,-2,5,-1,2,-1]
], dtype=float)

b1 = np.array([10,-5,8,4,-7,6,-3,9], dtype=float)

print("\n--- EJERCICIO 1 ---")
sol1 = gauss_jordan_pivot_determinante(A1,b1)
print("Solución:", sol1)


# -------------------------
# EJERCICIO 2 (9x9)
# -------------------------

A2 = np.array([
[3,-2,5,-1,4,2,-3,1,2],
[-2,4,-3,1,5,-1,2,-4,3],
[5,-1,2,-3,4,1,-2,3,-1],
[1,-3,4,-2,5,-1,2,-1,4],
[2,3,-1,4,-2,5,-3,1,-2],
[-3,2,4,-1,3,-2,5,-1,1],
[4,-1,3,2,-3,1,-2,5,-4],
[-1,5,-2,3,4,-1,2,-3,1],
[3,-2,5,-1,4,2,-3,1,-5]
], dtype=float)

b2 = np.array([-8,7,-6,5,12,-9,10,3,-2], dtype=float)

print("\n--- EJERCICIO 2 ---")
sol2 = gauss_jordan_pivot_determinante(A2,b2)
print("Solución:", sol2)


# -------------------------
# EJERCICIO 3 (10x10)
# -------------------------

A3 = np.array([
[2,-3,4,-1,5,-1,2,-1,3,-2],
[-3,2,5,-1,4,2,-3,1,-2,5],
[4,-1,3,2,-3,1,-2,5,-4,1],
[-1,5,-2,3,4,-1,2,-3,1,-5],
[3,-2,5,-1,4,2,-3,1,-5,2],
[-2,4,-3,1,5,-1,2,-4,3,-1],
[5,-1,2,-3,4,1,-2,3,-1,4],
[1,-3,4,-2,5,-1,2,-1,4,-3],
[2,3,-1,4,-2,5,-3,1,-2,1],
[-3,2,4,-1,3,-2,5,-1,1,-4]
], dtype=float)

b3 = np.array([11,-10,8,-6,7,-3,9,-5,6,-8], dtype=float)

print("\n--- EJERCICIO 3 ---")
sol3 = gauss_jordan_pivot_determinante(A3,b3)
print("Solución:", sol3)


# -----------------------------------
# OPCIÓN PARA QUE EL USUARIO INGRESE MATRIZ
# -----------------------------------

def resolver_usuario():

    n = int(input("\nIngrese el tamaño de la matriz (n): "))

    A = np.zeros((n,n))
    b = np.zeros(n)

    print("\nIngrese los coeficientes de la matriz A:")

    for i in range(n):
        for j in range(n):
            A[i,j] = float(input(f"A[{i+1},{j+1}] = "))

    print("\nIngrese los valores del vector b:")

    for i in range(n):
        b[i] = float(input(f"b[{i+1}] = "))

    solucion = gauss_jordan_pivot_determinante(A,b)

    if solucion is not None:
        print("Solución:", solucion)


# Preguntar al usuario
op = input("\n¿Deseas resolver tu propia matriz? (s/n): ")

if op.lower() == "s":
    resolver_usuario()