try:
    edad = int(
        input(
            "Ingresa tu edad (Y bien ingresada, porque si estuviesemos en C valemos):"
        )
    )

    if edad < 0:
        print("sentido Tu no lógica tiene, como este mensaje")
    else:
        print(f"Tu edad es {edad}")

except ValueError:
    print("Ingresa números, quieres que lo haga en C y el PC explote")
except Exception:
    print("No sé que hiciste, pero fue culpa tuya")
