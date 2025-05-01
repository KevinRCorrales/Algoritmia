Algoritmo bono
    definir salario, horas, bono_porcentaje, total como entero
    escribir"Ingrese el salario base y la cantidad de horas trabajadas: "
    leer salario, horas
    si horas > 40 entonces
        bono_porcentaje <- salario * 10 / 100
        total <- salario + bono_porcentaje
        imprimir"El salario total es: ", total
    SiNo
        imprimir"El salario se queda en: ", salario
    FinSi
FinAlgoritmo
