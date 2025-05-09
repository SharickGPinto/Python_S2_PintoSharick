def calcular_sueldo(horas):
    sueldo_bruto = horas * 20000
    desc_eps = sueldo_bruto * 0.04
    desc_pension = sueldo_bruto * 0.04
    sueldo_neto = sueldo_bruto - desc_eps - desc_pension
    return sueldo_bruto, desc_eps, desc_pension, sueldo_neto

def procesar_empleados():
    num_empleados = int(input("INGRESE EL NUMERO DE EMPLEADOS QUE VA A PROCESAR: "))
    sueldo_mayor = 0
    sueldo_menor = 0

    for i in range(1, num_empleados + 1):
        nombre = input(f"Ingrese el nombre del empleado {i}: ")
        horas = float(input("Ingrese las horas trabajadas del empleado: "))
        bruto, eps, pension, neto = calcular_sueldo(horas)

        if i == 1:
            sueldo_mayor = neto
            sueldo_menor = neto
        else:
            if neto > sueldo_mayor:
                sueldo_mayor = neto
            if neto < sueldo_menor:
                sueldo_menor = neto

        print(f"\nEmpleado: {nombre}")
        print(f"Horas trabajadas: {horas}")
        print(f"Sueldo bruto: {bruto}")
        print(f"Descuento EPS: {eps}")
        print(f"Descuento pensión: {pension}")
        print(f"Sueldo neto: {neto}")
        print("-" * 40)

    print(f"\nSueldo mayor: {sueldo_mayor}")
    print(f"Sueldo menor: {sueldo_menor}")

procesar_empleados()
