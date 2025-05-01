'''Algoritmo numero mayor
var 
    entero : numero1
    entero : numero2
inicio
    leer numero1
    numero1 <- ingresar "Ingrese un número"
    leer numero2
    numero2 <- ingresar "Ingrese otro número"
    si numero1 > numero2 entonces
        imprimir "El primer número es el mayor"
    si_no si numero1 < numero2 entonces
        imprimir "El primer número es el más pequeño"
    si_no
        imprimir "Los números son iguales"
    fin_si
fin'''

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

if numero1 > numero2:
    print("El primer número es el mayor.")
elif numero1 < numero2:
    print("El primer número es el más pequeño.")
else:
    print("Los números son iguales.")