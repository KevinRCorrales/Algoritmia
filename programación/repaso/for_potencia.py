x = int(input("Digite x: "))
n = int(input("Digite n: "))

resultado = 1

for i in range(n):
    resultado *= x #resultado = resultado * x

print(f"{x} elevado a la {n} => {resultado}")
