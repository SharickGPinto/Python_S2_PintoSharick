####################################################
#CUSTOM RAPPID 

#SE PIDE CUANTAS HAMBIRGUESAS DESEA EL CLIENTE
cantidad_hamburguesas =int(input("Hola, cuantas hamburgueas va a pedir?"))

#ahora vamos a poner acumuladores (SE DEBE REINICIAR POR CADA HAMBIRGUESA)

ingredientes = 0

#repetimos el pedido para cada hamburguesa
for i in range(1, cantidad_hamburguesas + 1):
    print (f"\n--- Hamburguesas #{i}---")

    opcion = input("Que tipo de pan desea? 1.centeno/2.avena")
    if opcion == "1" "centeno":
        valor_pan =+ 1000
    else:
        opcion == "2" "avena"
        valor_pan =+ 1500
    
    opcion =input("Cuanta carne desea? (1. 250 o 2. 300)")
    if opcion == "1":
        valor_carne =+ 5000
    else:
        valor_carne =+ 7000

    opcion=input("cuanto pollo desea? (1. 250 o 2. 350)")
    if opcion == "1":
        valor_pollo =+ 6500
    else:
        opcion == "2"
        valor_pollo =+ 7500

    opcion=input("caunto pollo desmechado desea? (1. 250 0 2. 350)")
    if opcion == "1":
        valor_pollo_desmechado =+ 6500
    else:
        opcion == "2"
        valor_pollo_desmechado =+ 7500
    
    opcion =input("cuantas tocinetas desesa 1. lonja o 2, lonjas")
    if opcion == "1":
        valor_tocineta =+ 1500
    else:
        opcion == "2"
        valor_tocineta =+ 2500

    opcion = input ("que tipo de papa frita desea? 1. francesa o 2, cascos")
    if opcion == "1":
        valor_papa =+ 5000
    else:
        opcion == "2"
        valor_papa =+ 6000
    opcion= input("que bebida desea? 1. gaseosa 2.cerveza 3.naranjada")
    if opcion == "1":
        valor_bebida =+ 5000
    elif opcion == "2":
        valor_bebida =+ 8000
    else:
        opcion == "3"
        valor_bebida =+ 9000

#CALCULAMOS EL PEDIDO
subtotal = valor_pan + valor_carne + valor_pollo + valor_pollo_desmechado + valor_tocineta + valor_papa + valor_bebida
total_sin_servicio = subtotal 
#YA ESTA MULTIPLICADO DENTRO DEL BUCLE
servicio = total_sin_servicio * 0.10
total_final = total_sin_servicio + servicio

#SE MUESTRA EL VALOR FINAL
print (f"EL TOTAL DE PAGAR, INCLUYENDO EL 10% DE SERVICIO, ES: {total_final}") 

