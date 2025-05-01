from random import randint

secreto = randint(1, 10)
intentos = 0

print("OJO: TIENES 3 INTENTOS PARA ADIVINAR EL NÚMERO ENTRE 1 Y 10")

while intentos < 3:
    respuesta = int(input("Ingresa tu número: "))
    intentos += 1
    if respuesta == secreto:
        print("Felicidades, has ganado")
        break
    elif respuesta < secreto:
        print("Más alto")
    else:
        print("Mas bajo")

    if intentos == 3:
        print("Perdiste")
