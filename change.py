def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass

    Gasto = float(input("Introduce un gasto:"))
    Recibido = int(input("Introduce un recibido:"))

    Vuelto = (Recibido) - (Gasto)
    Vuelto_pesos = int(Vuelto)
    Vuelto_centavos = float(Vuelto - Vuelto_pesos) * 100

    print("Ingresar gasto:")
    print(Gasto)
    print("Dinero recibido")
    print(Recibido)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(Vuelto_pesos)
    print("Centavos:")
    print(round(Vuelto_centavos))

