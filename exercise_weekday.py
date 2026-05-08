def weekday():
    dia = input()

    if not (dia == "sabado" or dia == "domingo"):
        print("Dia habil")
    else:
        print("Fin de semana")
