sw = 0

while sw == 0:
    n = float(input("Ingresa N: "))
    if n != int(n):
        print("""Dato no válido
Ejecute nuevamente""")
        sw = 1
    else:
        print(f"Correcto {n} es entero")