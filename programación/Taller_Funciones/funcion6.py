def triplete(num1, num2, num3):
    mayor = max(num1, num2, num3)
    if num1 < mayor and num2 < mayor and num3 == mayor:
        menor1 = num1
        menor2 = num2
    elif num1 < mayor and num2 == mayor and num3 < mayor:
        menor1 = num3
        menor2 = num2
    elif num1 == mayor and num2 < mayor and num3 < mayor:
        menor1 = num2
        menor2 = num3

    return menor1 ** 2 + menor2 ** 2 == mayor ** 2

print(triplete(3,4, 5))
print(triplete(13, 5, 12))
print(triplete(1, 2, 3))