# Algoritmo no funcional

'''
Algoritmo numero_central
var
    entero : numero1
    entero : numero2
    entero : numero3
inicio
    leer numero1
    numero1 <- ingresar “Ingrese el primer número”
    leer numero2
    numero2 <- ingresar “Ingrese el segundo número”
    leer numero3
    numero3 <- ingresar “Ingrese el tercer número”
    si numero1 > numero2 and numero1 < numero3 entonces
        imprimir "El numero1 es el número central"
    si_no si numero2 > numero1 and numero2 < numero3 entonces
        imprimir "El numero2 es el número central"
    si_no si numero3 > numero1 and numero3 < numero2 entonces
        imprimir "El numero3 es el número central"
    si_no
        imprimir "Todos los números son iguales"
    fin_si
fin
'''

print("A continuación probarás el algoritmo no funcional...")

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

if numero1 > numero2 and numero1 < numero3:
    print(f"El {numero1} es el número central")
elif numero2 > numero1 and numero2 < numero3:
    print(f"El {numero2} es el número central")
elif numero3 > numero1 and numero3 < numero2:
    print(f"El {numero3} es el número central")
else:
    print("Todos los números son iguales")



# Algoritmo funcional

'''
Algoritmo numero_central
var
    entero : numero1
    entero : numero2
    entero : numero3
    entero : maxnum
    entero : minnum 
inicio
    leer numero1
    numero1 <- ingresar “Ingrese el primer número”
    leer numero2
    numero2 <- ingresar “Ingrese el segundo número”
    leer numero3
    numero3 <- ingresar “Ingrese el tercer número”
    leer maxnum
    maxnum <- max(numero1, numero2, numero3)
    minnum <- min(numero1, numero2, numero3)
    si numero1 != maxnum and numero1 != minnum entonces
        imprimir "El numero1 es el número central"
    si_no si numero2 != maxnum and numero2 != minnum entonces
        imprimir "El numero2 es el número central"
    si_no si numero3 != maxnum and numero3 != minnum entonces
        imprimir "El numero3 es el número central"
    si_no
        imprimir "Todos los números son iguales"
    fin_si
fin
'''

print("A continuación probarás el algoritmo funcional...")

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

maxnum = max(numero1, numero2, numero3)
minnum = min(numero1, numero2, numero3)

if numero1 != maxnum and numero1 != minnum:
    print(f"El {numero1} es el número central")
elif numero2 != maxnum and numero2 != minnum:
    print(f"El {numero2} es el número central")
elif numero3 != maxnum and numero3 != minnum:
    print(f"El {numero3} es el número central")
else:
    print("Todos los números son iguales")