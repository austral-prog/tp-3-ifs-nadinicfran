def age_check():
    edad = int(input())
    limite = int(input())

    if edad <= 0 or limite <= 0:
        print("Entrada invalida")
    elif edad >= limite:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
