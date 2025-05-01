dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

if dia == 30 and mes == 12:
    dia = 1
    mes = 1
    anio += 1

elif dia == 30 and mes < 12:
    dia = 1
    mes += 1

else:
    dia += 1

print(f"La fecha siguiente es {dia}/{mes}/{anio}")