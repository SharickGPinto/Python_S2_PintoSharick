#######################################################################################
#NOMINA 

num_empleados =int(input("INGRESE EL NUMERO DE EMPLEADOS QUE VA A PROCESAR:"))

#INIALIZACION DE VARIABLES PARA LOS SUELDOS MAYOR Y MENOR

sueldo_menor = 0
sueldo_mayor = 0

#BUCLE PARA PROCESAR CADA EMPLEADO

for i in range(1, num_empleados + 1):
    nombre = input(f"ingrese el nombre del empleado  {i} ")
    horas = int(input("Ingrese las horas trabajadas del empleado:"))

    sueldo_bruto = horas * 20000
    desc_eps = sueldo_bruto * 4// 100
    des_pension = sueldo_bruto *4// 100 
    sueldo_neto = sueldo_bruto - des_pension - desc_eps

    #ASIGNAR EL PRIMER SUELDO NETO COMO BASE PARA COMPARACION

    if i == 1:
        sueldo_mayor = sueldo_neto
        sueldo_menor = sueldo_neto
    else:
        if sueldo_neto > sueldo_mayor:
            sueldo_mayor = sueldo_neto
        if sueldo_neto < sueldo_menor:
            sueldo_menor = sueldo_neto

###########################
###########################
#AHORA SE DEBE MOSTRAR LOS RESULTADOS DEL EMPLEADO

    print(f"Nombre del empleado: {nombre}")
    print(f"Horas trabajadas: {horas}")
    print(f"Sueldo bruto: {sueldo_bruto} " )
    print(f"Descuento de la EPS: {desc_eps}")
    print(f"Descuento de la pension {des_pension}")
    print(f"sueldo neto: {sueldo_neto}")
    print("---------------------------------------------------------------------")

#MOSTRAR LOS SUELDOS MAYOR Y MENOR
print(f"EL SUELDO MAYOR ES: {sueldo_mayor}")
print(f"EL SUELDO MENOR ES: {sueldo_menor}") 

#####################################
#RECORDATORIO INT PARA NUMEROS ENTEROS Y SI ES 0.04 PASARLO A LA FORMULA COMO 4 // 100
#FLOAT ES PARA NUMERIOS FRACCIONADOS COMO 0.004 O 37.5
