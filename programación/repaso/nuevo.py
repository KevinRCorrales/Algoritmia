total = 0
numero = 0
suma = 0

total = int(input("Cantidad de números: "))

for i in range(total):
    numero = int(input("Digite un número: "))
    suma += numero 
    
print(f"La suma de los {total} números es: {suma}")
