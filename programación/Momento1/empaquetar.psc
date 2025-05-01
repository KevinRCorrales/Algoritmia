Algoritmo empaquetar
	definir galletas, cajas, paquetes, galletas_sueltas, empacadas, paquetes_caja, paquetes_sueltos Como Entero
	escribir"Ingrese la cantidad total de galletas producidas: "
	leer galletas
	paquetes <- galletas div 24
	empacadas <- 24 * paquetes
	galletas_sueltas <- galletas - empacadas
	cajas <- paquetes div 12
	paquetes_caja <- 12 * cajas
	paquetes_sueltos <- paquetes - paquetes_caja
	imprimir"Cajas completas: ", cajas
	imprimir"Paquetes adicionales: ", paquetes_sueltos
	imprimir"Galletas sueltas: ", galletas_sueltas
FinAlgoritmo
