salario = int(input("Ingrese el salario base: "))
horas = int(input("Ingrese la cantidad de horas trabajadas: "))

if horas > 40:
    bono_porcentaje = salario * 10 / 100
    total = salario + bono_porcentaje
    print(f"El salario total es: {total}")

else:
    print(f"El salario se queda en: {salario}")