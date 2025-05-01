Algoritmo comercio
	definir articulos_A, articulos_B, dinero_A, dinero_B, precio, num_articulos, total Como Entero
	definir ficha como Caracter
	definir continuar Como Logico
	articulos_A <- 0
	articulos_B <- 0
	dinero_A <- 0
	dinero_B <- 0
	continuar <- Verdadero
	
	mientras continuar Hacer
		Escribir "Ingresa el tipo de ficha: "; leer ficha
		si ficha == "A" o ficha == "B" Entonces
			Escribir "Ingresa el precio unitario: ";leer precio
			Escribir "Ingresa el número de artículos: ";leer num_articulos
			total <- precio * num_articulos
			si ficha == "A" Entonces
				articulos_A <- articulos_A + num_articulos
				dinero_A <- dinero_A + total
			sino 
				articulos_B <- articulos_B + num_articulos
				dinero_B <- dinero_B + total
			FinSi
		SiNo
			continuar <- Falso
		FinSi
	FinMientras
	
	escribir "El número de artículos categoría A es: ", articulos_A
	escribir "El importe total de artículos en A es: ", dinero_A
	escribir "El número de artículos categoría B es: ", articulos_B
	escribir "El importe total de artículos en B es: ", dinero_B
FinAlgoritmo
