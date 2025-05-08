def conversion(anios):
    if anios < 0:
        return "Error: no se puede introducir minutos negativos."
    else:
        dias = round(anios * 365)
        return dias

print(conversion(65))
print(conversion(0))
print(conversion(20))
print(conversion(-20))