# Función que calcula distintos tipos de error
def calcular_errores(x, y, valor_real):
    # Diferencia calculada por la máquina
    diferencia = x - y
    # Error absoluto
    error_abs = abs(valor_real - diferencia)
    # Error relativo
    error_rel = error_abs / abs(valor_real)
    # Error porcentual
    error_pct = error_rel * 100
    # Mostrar resultados
    print(f"Diferencia: {diferencia}")
    print(f"Error absoluto: {error_abs}")
    print(f"Error relativo: {error_rel}")
    print(f"Error porcentual: {error_pct}%")
    return error_abs, error_rel
# Casos de prueba
valores = [
    (1.0000001, 1.0000000, 0.0000001),
    (1.000000000000001, 1.000000000000000, 0.000000000000001)
]
# Evaluación de cada caso
for x, y, real in valores:
    print(f"\nPara x={x}, y={y}:")
    calcular_errores(x, y, real)