positivos = 0
negativos = 0

while True:
    numero = int(input("Ingresa un número: "))
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1
    else:
        break

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
