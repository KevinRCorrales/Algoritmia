articulos_A = 0
articulos_B = 0

dinero_A = 0
dinero_B = 0

while True:
    ficha = input("Ingresa el tipo de ficha: ").strip().lower()
    if ficha == "a" or ficha == "b":
        precio = int(input("Ingresa el precio unitario: "))
        num_articulos = int(input("Ingresa el número de artículos: "))
        total = precio * num_articulos
        if ficha == "a":
            articulos_A+=num_articulos
            dinero_A+=total
        else:
            articulos_B+=num_articulos
            dinero_B+=total
    else:
        break

print(f"""El número de artículos categoría A es: {articulos_A}
El importe total de artículos en A es: {dinero_A}

El número de artículos categoría B es: {articulos_B}
El importe total de artículos en B es: {dinero_B}""")