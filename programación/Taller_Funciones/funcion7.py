def contar(cadena):
    letras = cadena.lower()
    vocales = 0
    for letra in letras:
        vocal = ["a","e","i","o","u", "á", "é", "í", "ó", "ú"]
        for voc in vocal:
            if voc == letra:
                vocales += 1
    return vocales

print(contar("Celebración"))
print(contar("Palma"))
print(contar("Predicción"))
print(contar("bcd"))
print(contar("Abcd"))