n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))

maxn = (n1 + n2) / 2

while (n2 != 999) or (n1 != 999):
    n1 = int(input("Ingresa el primer número: "))
    n2 = int(input("Ingresa el segundo número: "))
    m = (n1 + n2) / 2
    if m > maxn:
        maxn = m

print(f"Media máxima = {maxn}")