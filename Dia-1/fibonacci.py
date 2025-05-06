###################################################################
#SERIE DE FIBONACCI

n = int(input("Ingrese la cantidad de términos: "))

a, b = 0, 1
print("Serie Fibonacci:")
print(a)
if n > 1:
    print(b)

for i in range(3, n + 1):
    c = a + b
    print(c)
    a = b
    b = c