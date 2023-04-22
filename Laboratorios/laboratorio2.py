import random

nro = int(input("Ingrese un numero que multiplique a la matriz: "))
filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

matriz = [[random.randint(0, 10) for i in range(columnas)] for j in range(filas)]

print("La matriz uno es")
for i in range(columnas):
    for j in range(filas):
        print(matriz[i][j])

print()

multi = [[matriz[i][j]*nro] for i in range(columnas) for j in range(filas)]

print(multi)