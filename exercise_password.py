def password():
    clave = input()

    tiene_numero = (
        "0" in clave or "1" in clave or "2" in clave or "3" in clave or "4" in clave or
        "5" in clave or "6" in clave or "7" in clave or "8" in clave or "9" in clave
    )

    errores = False

    if len(clave) < 8:
        print("Contraseña muy corta")
        errores = True

    if not tiene_numero:
        print("Debe contener un numero")
        errores = True

    if not errores:
        print("Contraseña valida")
