calificacion = int(input("Ingrese la calificación: "))

if calificacion < 60:
    print("Reprobaste.")
elif calificacion >= 60 and calificacion <= 69:
    print("Pasaste raspando con D.")
elif calificacion >= 70 and calificacion <= 79:
    print("Aprobaste con C.")
elif calificacion >= 80 and calificacion <= 89:
    print("Aprobaste con B.")
else:
    print("Aprobaste con A.")
