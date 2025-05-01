import time
base = int(input("Ingresa el número base: "))
base2 = base
limite = int(input("Ingresa el límite: "))
multiplicar = 1
if base < 1 or limite < 1:
    print("Que pasa aquí!? Crees que si andas de chistoso poniendo eso en C el PC sobrevive?")
else:
    while True:
        resultado = base*multiplicar
        if resultado < limite:
            multiplicar+=1
            print(resultado)
            time.sleep(0.1)
        else:
            break
        

print(f"Se encontraron {multiplicar-1} múltiplos de {base2} entre 1 y {limite}.")
        
