Algoritmo clima
	definir dias, erroneos, minima, maxima, correctos, max_suma, min_suma Como Entero
	definir porcentaje, media_max, media_min Como Real
	dias <- 0
	erroneos <- 0
	correctos <- 0
	max_suma <- 0
	min_suma <- 0
	escribir "Ingrese la temperatura m�nima: "
	leer minima
	escribir "Ingrese la temperatura m�xima: "
	leer maxima
	mientras minima =! 0 o maxima =! 0 Hacer
		dias <- dias + 1
		si minima == 9 o maxima == 9 Entonces
			erroneos <- erroneos + 1
			escribir "Se cometi� un error aqu�..."
		sino 
			correctos <- correctos + 1
			max_suma <- max_suma + maxima
			min_suma <- min_suma + minima
			escribir "Se ingresaron resultados correctos..."
		FinSi
		escribir "Ingrese la temperatura m�nima: "
		leer minima
		escribir "Ingrese la temperatura m�xima: "
		leer maxima
	FinMientras
	porcentaje <- (erroneos / dias) * 100
	media_max <- max_suma / correctos
	media_min <- min_suma / correctos
	escribir "Las temperaturas se proporcionaron durante ",dias, " d�as."
	escribir "La media de las temperaturas m�ximas es: ",media_max," y la media de las temperaturas m�nimas es :", media_min
	escribir "El n�mero de errores fue: ",erroneos," lo que represent� un pocentaje del ",porcentaje,"% de errores."
FinAlgoritmo
