def animales(pollos, vacas, cerdos):
    p_pollos = pollos * 2
    p_vacas = vacas * 4
    p_cerdos = cerdos * 4
    total = p_pollos + p_vacas + p_cerdos
    return total

print(animales(2,3, 5))
print(animales(1, 2, 3))
print(animales(5, 2, 8))