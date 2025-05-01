i = 1 
numero = int(input(f"{i}: Ingresa un número: "))
maxn = numero
minn = numero

for i in range(2, 101):
    numero = int(input(f"{i}: Ingresa un número: "))
    if numero > maxn:
        maxn = numero
    elif numero < minn:
        minn = numero

print(f"Maximo: {maxn}, Minimo: {minn}")