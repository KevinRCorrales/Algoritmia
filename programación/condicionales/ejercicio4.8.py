numero1 = int(input("Ingresar el primer número: "))
numero2 = int(input("Ingresar el segundo número: "))
if numero1 % numero2 == 0:
    print(f"el {numero2} es divisor del {numero1}.")
elif numero2 % numero1 == 0:
    print(f"el {numero1} es divisor del {numero2}.")
else:
    print("Ningún número ingresado es divisor del otro.")