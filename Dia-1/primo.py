########################################################
#NUMERO PRIMO

num = int(input("INGRESE EL NUMERO: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

if contador == 2:
    print(num, "ES PRIMO")
else:
    print(num, "NO ES PRIMO")