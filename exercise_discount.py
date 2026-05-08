def discount():
    precio = float(input())
    cantidad = int(input())

    subtotal = precio * cantidad

    if cantidad >= 10:
        porcentaje = 20
    elif cantidad >= 5:
        porcentaje = 10
    else:
        porcentaje = 0

    monto_descuento = subtotal * porcentaje / 100
    total_final = subtotal - monto_descuento

    print(f"Subtotal: {subtotal}")
    print(f"Descuento aplicado: {porcentaje}%")
    print(f"Monto de descuento: {monto_descuento}")
    print(f"Total final: {total_final}")
