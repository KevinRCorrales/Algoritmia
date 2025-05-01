import time
cuenta = 2
imprimidos = 1
while cuenta <= 1000:
    print(cuenta)
    time.sleep(0.2)
    imprimidos+=1 
    cuenta+=2

print(f"Se imprimieron {imprimidos} números")
