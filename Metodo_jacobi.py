import numpy as np
import matplotlib.pyplot as plt

def jacobi(A, b, tol=1e-6, max_iter=100):

    n = len(A)
    x = np.zeros(n)

    sol_exacta = np.linalg.solve(A,b)

    errores_abs=[]
    errores_rel=[]
    errores_cuad=[]

    tabla=[]

    for k in range(max_iter):

        x_new=np.zeros(n)

        for i in range(n):

            suma=0

            for j in range(n):

                if j!=i:
                    suma+=A[i][j]*x[j]

            x_new[i]=(b[i]-suma)/A[i][i]

        error_abs=np.linalg.norm(x_new-sol_exacta,1)
        error_rel=error_abs/np.linalg.norm(sol_exacta,1)
        error_cuad=np.linalg.norm(x_new-sol_exacta,2)

        errores_abs.append(error_abs)
        errores_rel.append(error_rel)
        errores_cuad.append(error_cuad)

        tabla.append(x_new.copy())

        if np.linalg.norm(x_new-x,np.inf)<tol:
            break

        x=x_new

    return x_new,sol_exacta,errores_abs,errores_rel,errores_cuad,tabla


def graficar(errores_abs,errores_rel,errores_cuad):

    plt.figure()

    plt.plot(errores_abs,label="Error absoluto")
    plt.plot(errores_rel,label="Error relativo")
    plt.plot(errores_cuad,label="Error cuadrático")

    plt.yscale("log")

    plt.xlabel("Iteraciones")
    plt.ylabel("Error")
    plt.title("Convergencia del método de Jacobi")
    plt.legend()
    plt.grid()

    plt.show()


def resolver(A,b):

    sol,exacta,eabs,erel,ecua,tabla=jacobi(A,b)

    print("\nSolución aproximada:")
    print(sol)

    print("\nSolución exacta:")
    print(exacta)

    print("\nTabla de iteraciones")

    for i,fila in enumerate(tabla):
        print("Iter",i+1,":",fila)

    graficar(eabs,erel,ecua)


# -------------------------
# EJERCICIO 1
# -------------------------

A1=np.array([
[10,-1,2,0,0],
[-1,11,-1,3,0],
[2,-1,10,-1,0],
[0,-1,3,8,-2],
[0,0,2,-2,10]
],dtype=float)

b1=np.array([6,25,-11,15,-10],dtype=float)

resolver(A1,b1)


# -------------------------
# EJERCICIO 2
# -------------------------

A2=np.array([
[8,2,-1,0,0,0],
[3,15,-2,1,0,0],
[0,-2,12,2,-1,0],
[0,1,-1,9,-2,1],
[0,0,-2,3,14,1],
[0,0,0,1,-2,10]
],dtype=float)

b2=np.array([10,24,-18,16,-9,22],dtype=float)

resolver(A2,b2)


# -------------------------
# EJERCICIO 3
# -------------------------

A3=np.array([
[12,-2,1,0,0,0,0],
[-3,18,-4,2,0,0,0],
[1,-2,16,-1,1,0,0],
[0,2,-1,11,-3,1,0],
[0,0,-2,4,15,-2,0],
[0,0,0,1,-3,2,13],
[0,0,0,0,0,0,13]
],dtype=float)

b3=np.array([20,35,-5,19,-12,0,25],dtype=float)

resolver(A3,b3)


# -------------------------
# UN SISTEMA PERSONALIZADO POR LA PERSONA
# -------------------------

def sistema_usuario():

    n=int(input("Numero de ecuaciones: "))

    A=np.zeros((n,n))
    b=np.zeros(n)

    print("Introduce la matriz A")

    for i in range(n):
        for j in range(n):
            A[i][j]=float(input(f"A[{i+1},{j+1}]: "))

    print("Introduce el vector b")

    for i in range(n):
        b[i]=float(input(f"b[{i+1}]: "))

    resolver(A,b)


# Descomentar si se quiere usar
# sistema_usuario()