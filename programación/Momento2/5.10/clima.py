dias = 0 
erroneos = 0
correctos = 0
max_suma = 0
min_suma = 0

minima = int(input("Ingresa la temperatura mínima: "))
maxima = int(input("Ingresa la temperatura máxima: "))

while minima != 0 or maxima != 0:
    dias += 1
    
    if minima == 9 or maxima == 9:
        erroneos += 1
        print("Se cometió un error aquí...")
    else:
        correctos += 1
        max_suma += maxima
        min_suma += minima
        print("Se ingresaron resultados correctos...")

    minima = int(input("Ingresa la temperatura mínima: "))
    maxima = int(input("Ingresa la temperatura máxima: "))

porcentaje = (erroneos/dias)*100
media_max = max_suma / correctos 
media_min = min_suma / correctos

print(f"""Las temperaturas se proporcionaron durante {dias} días.
La media de las temperaturas máximas es: {media_max}, y la media de las temperaturas mínimas es: {media_min}
El número de errores fue: {erroneos} lo que representó en porcentaje del {porcentaje}% de errores.""")