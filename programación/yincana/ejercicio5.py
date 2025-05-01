saldo = int(input("Saldo inicial: "))
print("""Opción 1: Salir
Opción 2: Retirar
Opción 3: Depositar""")
while True:
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        break
    elif opcion == 2:
        monto = int(input("Monto: "))
        if monto < saldo or monto == saldo:
            saldo -= monto
            print(f"Has retirado ${monto}. Tu nuevo saldo es ${saldo}.")
        else:
            print("Fondos insuficientes.")
    elif opcion == 3:
        monto = int(input("Monto: "))
        saldo += monto
        print(f"Has depositado ${monto}. Tu nuevo saldo es ${saldo}.")
    else:
        print("Opción no válida vuelva a intentarlo.")
