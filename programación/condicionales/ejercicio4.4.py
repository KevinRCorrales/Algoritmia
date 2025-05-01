import math

numero = int(input("Ingrese un número: "))
if numero >= 0:
    print(math.sqrt(numero))
else:
    print("El número ingresado es negativo, intente nuevamente.")