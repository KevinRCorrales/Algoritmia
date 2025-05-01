tarifa_base = 3.00
kilometros = float(input("Ingrese la cantidad de kilómetros recorridos: "))
extra = kilometros * 1.50
total = tarifa_base + extra

print(f"El total a cobrar es: {total}")