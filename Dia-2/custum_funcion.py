def seleccionar_ingredientes():
    total = 0

    opcion = input("¿Qué tipo de pan desea? (1. centeno / 2. avena): ")
    total += 1000 if opcion == "1" else 1500

    opcion = input("¿Cuánta carne desea? (1. 250 / 2. 300): ")
    total += 5000 if opcion == "1" else 7000

    opcion = input("¿Cuánto pollo desea? (1. 250 / 2. 350): ")
    total += 6500 if opcion == "1" else 7500

    opcion = input("¿Cuánto pollo desmechado desea? (1. 250 / 2. 350): ")
    total += 6500 if opcion == "1" else 7500

    opcion = input("¿Cuántas tocinetas desea? (1. lonja / 2. lonjas): ")
    total += 1500 if opcion == "1" else 2500

    opcion = input("¿Qué tipo de papa frita desea? (1. francesa / 2. cascos): ")
    total += 5000 if opcion == "1" else 6000

    opcion = input("¿Qué bebida desea? (1. gaseosa / 2. cerveza / 3. naranjada): ")
    if opcion == "1":
        total += 5000
    elif opcion == "2":
        total += 8000
    else:
        total += 9000

    return total

def procesar_pedido():
    cantidad = int(input("¿Cuántas hamburguesas desea pedir?: "))
    subtotal = 0

    for i in range(1, cantidad + 1):
        print(f"\n--- Hamburguesa #{i} ---")
        subtotal += seleccionar_ingredientes()

    servicio = subtotal * 0.10
    total_final = subtotal + servicio
    print(f"\nEL TOTAL A PAGAR, INCLUYENDO EL 10% DE SERVICIO, ES: ${total_final:.0f}")

procesar_pedido()
