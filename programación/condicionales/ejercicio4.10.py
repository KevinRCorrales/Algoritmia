calificacion = int(input("Ingrese la calificación: "))
if calificacion >= 90:
    letra = "A"
elif calificacion < 90 and calificacion >= 80:
    letra = "B"
elif calificacion < 80 and calificacion >= 70:
    letra = "C"
elif calificacion < 70 and calificacion >= 69:
    letra = "D"
else:
    letra = "F"

print(f"La calificación correspondiente es {letra}")