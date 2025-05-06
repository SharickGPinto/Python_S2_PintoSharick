########################################################################
#SACAR EL PROMEDIO DE UNA LISTA

n = int(input("¿Cuántos números ingresará?: "))
suma = 0

for i in range(n):
    num = float(input(f"Ingrese el número {i + 1}: "))
    suma += num

promedio = suma / n
print("El promedio es:", promedio)