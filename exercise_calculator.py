def calculator():
    numero1 = float(input())
    numero2 = float(input())
    operacion = input()

    if operacion == "+":
        print(f"Resultado: {numero1 + numero2}")
    elif operacion == "-":
        print(f"Resultado: {numero1 - numero2}")
    elif operacion == "*":
        print(f"Resultado: {numero1 * numero2}")
    elif operacion == "/":
        if numero2 == 0:
            print("Error: division por cero")
        else:
            print(f"Resultado: {numero1 / numero2}")
    else:
        print("Operacion invalida")
