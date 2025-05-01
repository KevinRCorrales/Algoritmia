peso = float(input("Ingrese el peso: "))
if peso < 40:
    print("Tiene peso muy bajo.")
elif peso >= 40 and peso <= 50:
    print("Tiene peso bajo.")
elif peso > 50 and peso < 60:
    print("Tiene peso medio o ideal.")
else:
    print("Tiene peso alto o sobrepeso.")