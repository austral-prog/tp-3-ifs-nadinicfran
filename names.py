def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """


    nombre = input("ingrese el nombre:")
    apellido = input("ingrese el apellido:")
    nombre_completo = (nombre + " " + apellido)

    print(nombre_completo.lower())
    print(nombre_completo.title())
    print(nombre_completo.upper())
    print("\t" + nombre_completo.lower())




