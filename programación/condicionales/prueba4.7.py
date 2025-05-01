pesos = {
    "peso1" : 62,
    "peso2" : 75,
    "peso3" : 58,
    "peso4" : 80,
    "peso5" : 45,
}

for peso, valor in pesos.items():
    if  valor < 40:
        print("Tiene peso muy bajo.")
    elif valor >= 40 and valor <= 50:
        print("Tiene peso bajo.")
    elif valor > 50 and valor < 60:
        print("Tiene peso medio o ideal.")
    else:
        print("Tiene peso alto o sobrepeso.")