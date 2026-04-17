from operator import truediv


def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    pass

    contrasena = input("Ingrese su contrasena: ")

    longitud = len(contrasena) >= 8
    numero = False
    for digito in "0123456789":
        if digito in contrasena:
            numero = True

    if longitud and numero:
        print("Contraseña valida")
    else:
        if not longitud:
            print("Contraseña muy corta")
        if not numero:
            print("Debe contener un numero")

