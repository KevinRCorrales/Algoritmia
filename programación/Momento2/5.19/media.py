nombre = input("Ingrese el nombre del estudiante: ")

while nombre != "***":
    basic = float(input("Ingrese la nota de BASIC: "))
    pascal = float(input("Ingrese la nota de pascal: "))
    fortran = float(input("Ingrese la nota de FORTRAN: "))
    media = (basic + pascal + fortran) / 3
    print(f"{nombre}, {media}")

    nombre = input("Ingrese el nombre del estudiante: ")