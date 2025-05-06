######################################################
#FACTORIAL DE UN NUMERO
 
num=int(input("INGRESE UN NUMERO"))
if num < 0:
    print("EL FACTORIAL NO ESTA DEFINIDO PARA ESTE NUMEROS NEGSTIVOS")
else:
    factorial = 1 
#EL FACTORIAL SE CALCULA MULTIPLICANDO DESDE 1 HASTA NUM
for i in range(1, num + 1):
    factorial *=i

print("EL FACTORIA ES:", factorial)

#DA EL RESULTADO