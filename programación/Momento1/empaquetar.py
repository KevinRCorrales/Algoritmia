galletas = int(input("Ingrese la cantidad total de galletas producidas: "))
paquetes = galletas // 24
empacadas = 24 * paquetes
galletas_sueltas = galletas - empacadas
cajas = paquetes // 12
paquetes_caja = 12 * cajas
paquetes_sueltos = paquetes - paquetes_caja
print(f"""Cajas completas: {cajas}
Paquetes adicionales: {paquetes_sueltos}
Galletas sueltas: {galletas_sueltas}""")