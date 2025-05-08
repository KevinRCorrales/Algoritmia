def reemplazar(cadena, caracter):
    vocales = ["a","e","i","o","u", "á", "é", "í", "ó", "ú"]
    cadena_reemplazada = ""
    for letra in cadena:
        if letra in vocales:
            cadena_reemplazada += caracter
        else:
            cadena_reemplazada += letra
    return cadena_reemplazada


print(reemplazar("el oso hormiguero", "#"))
print(reemplazar("minnie mouse", "?"))
print(reemplazar("shakespeare", "*"))