def calcular(n1, ope, n2):
    if ope == "+":
        return n1 + n2
    elif ope == "-":
        return n1 - n2
    elif ope == "*":
        return n1 * n2
    else:
        try:
            return n1 / n2
        except ZeroDivisionError as e:
            return f"ERROR: {e}"

print(calcular(5, "*", -8))
print(calcular(-7, "+", 34))
print(calcular(16, "/", 4))
print(calcular(5, "/", 0))
print(calcular(5, "-", 3))