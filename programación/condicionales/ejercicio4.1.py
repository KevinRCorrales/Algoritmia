print("Ejercicio A")

angulo = int(input("Ingrese la medida del ángulo: "))
if angulo == 90:
    print("El ángulo es un ángulo recto.")
else:
    print("El ángulo no es un ángulo recto.")

print("Ejercicio B")

temperatura = int(input("Ingrese la temperatura: "))
if temperatura > 100:
    print("Por encima del punto de ebullición del agua.")
else:
    print("Por debajo del punto de ebullición del agua.")

print("Ejercicio C")

numero = int(input("Ingrese un número: "))
positivos = 0
negativos = 0
if numero > 0:
    positivos += numero
    print(positivos)
else:
    negativos += numero
    print(negativos)

print("Ejercicio D")

x = int(input("Ingrese un valor para x: "))
y = int(input("Ingrese un valor para y: "))
z = int(input("Ingrese un valor para z: "))
if x > y and z < 20:
    p = int(input("Ingrese un valor para p: "))
else:
    print("No se cumple la condición")

print("Ejercicio D")

distancia = int(input("Ingrese la distancia: "))
if distancia > 20 and distancia < 35:
    tiempo = int(input("Ingrese el tiempo: "))
else:
    print("No se cumple la condición")