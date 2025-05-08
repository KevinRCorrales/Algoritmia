def conversion(min):
    if min <0:
        return "Error: no se puede introducir minutos negativos."
    else:
        return min * 60

print(conversion(5))
print(conversion(3))
print(conversion(2))
print(conversion(-9))