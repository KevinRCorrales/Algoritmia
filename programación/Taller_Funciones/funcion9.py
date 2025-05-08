def contar(numero):
    digitos = 0
    cadena = str(numero)
    for letra in cadena:
        if letra.isdigit():
            digitos += 1
    return digitos

print(contar(10))
print(contar(5000))
print(contar(0))
print(contar(-1))