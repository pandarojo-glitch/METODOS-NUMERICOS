# Inicializamos con un valor grande
epsilon = 1.0
# Contador de iteraciones
iteracion = 0
# Mientras la suma siga siendo distinta de 1.0
while 1.0 + epsilon != 1.0:
    # Reducimos epsilon a la mitad
    epsilon /= 2
    # Aumentamos el contador
    iteracion += 1
    # Mostramos el valor actual
    print(f"Iteracion: {iteracion}, Precisión de máquina: {epsilon}")
# Regresamos al último valor válido
epsilon *= 2
# Muestra la precisión de la máquina final
print(f"Precisión de máquina: {epsilon}")
