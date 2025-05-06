#################################################
#PARA ENCONTRAR EL NUMERO MAYOR DE 3 NUMEROS####
#SE PIDEN LOS 3 NUMEROS AL USUARIO PARA CONVERTIRLOS EN FLOAT

a =float(input("INGRESE EL PRIMER NUMERO"))
b =float(input("INGRESE EL SEGUNDO NUMERO"))
c =float(input("INGRESE EL TERCER NUMERO"))

#SE COMPARAN LOS NUMEROS USANDO if - elif - else
if a > b and a > c :
    print("EL NUMERO MAYOR ES:", a)
elif b > c:
    print ("EL NUMERO MAYOR ES:", b)
else:
    print ("EL NUMERO MAYOR ES ", c)

#DA EL RESULTADO 