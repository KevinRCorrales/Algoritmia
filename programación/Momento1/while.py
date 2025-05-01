n = 0
total = 0
numero = 0
suma = 0
orden = 0

n = int(input("Cantidad de números: "))
total = n
while(total > 0):
    orden += 1
    numero = int(input(f"Ingrese el número {orden}: "))
    suma += numero
    total -= 1
print(f"La suma de los {n} números es {suma}")

n = 0
total = 0
numero = 0
suma = 0
 
#pedir n (cantidad de números) por teclado
n = int(input("Cantidad de números:"))
total = n
while(total > 0):
    numero = int(input("Digite un número:"))
    suma += numero # suma = suma + numero
    total -= 1 #total = total - 1
 
#forma_1
print("1. La suma de los " , str(n) , " números es: " , str(suma))
#forma_2
print(f"2. La suma de los {n} números es: {suma}")
#Condicinal dentro del format
print(f"La suma es: {suma} -> {'Par' if suma%2 == 0 else 'Impar'}")
#forma_3
print("3. La suma de los {} números es: {}".format(n,suma))