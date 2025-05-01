Algoritmo dia_siguiente
	definir dia, mes, anio Como Enteros
	escribir"Ingrese dia: "
	leer dia
	escribir"Ingrese mes: "
	leer mes
	escribir"Ingrese anio: "
	leer anio
	si dia=30 y mes=12 Entonces
		dia <- 1
		mes <- 1
		anio <- anio + 1
	SiNo
		si dia=30 y mes < 12 entonces
			dia <- 1
			mes <- mes + 1
		SiNo
			dia <- dia + 1
		FinSI
	FinSi
	mostrar"La fecha siguiente es ", dia, "/", mes, "/", anio
FinAlgoritmo
