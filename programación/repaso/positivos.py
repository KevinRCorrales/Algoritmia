suma = 0

while True:
    numero = int(input("Ingresa un número: "))
    if numero > 0:
        suma += numero
    elif numero < 0:
        print("Jóven, estamos produciendo no quitando")
        continue
    else:
        break

print(f"La suma de los positivos es: {suma}")
