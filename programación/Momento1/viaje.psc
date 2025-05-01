Algoritmo viaje_taxi
	definir tarifa_base, kilometros, extra, total como Real
	tarifa_base <- 3.00
	escribir"Ingrese la cantidad de kilómetros recorridos: "
	leer kilometros
	extra <- kilometros * 1.50
	total <- tarifa_base + extra
	imprimir"El total a cobrar es: ", total
FinAlgoritmo
