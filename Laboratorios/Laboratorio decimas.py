import numpy as np

#Se pide al usuario que ingrese las filas y columnas de la primera matriz
filas_matriz_1 = int(input("Ingrese la cantidad de filas de la primera matriz: "))
columnas_matriz_1 = int(input("Ingrese la cantidad de columnas de la primera matriz: "))

#Se pide al usuario que ingrese las filas y columnas de la segunda matriz
filas_matriz_2 = int(input("Ingrese la cantidad de filas de la segunda matriz: "))
columnas_matriz_2 = int(input("Ingrese la cantidad de columnas de la segunda matriz: "))

matriz_1 = np.zeros((filas_matriz_1, columnas_matriz_1))
for i in range(filas_matriz_1):
    for j in range(columnas_matriz_1):
        matriz_1[i][j] = int(input("Introduzca los valores para la matriz 1: "))

print(matriz_1)

matriz_2 = np.zeros((filas_matriz_2, columnas_matriz_2))
for i in range(filas_matriz_2):
    for j in range(columnas_matriz_2):
        matriz_2[i][j] = int(input("Introduzca los valores para la matriz 2: "))

print(matriz_2)

suma = [[matriz_1[i][j] + matriz_2[i][j] for i in range(columnas_matriz_1)] for j in range(filas_matriz_1)]

print(suma)

resta = [[matriz_1[i][j] - matriz_2[i][j] for i in range(columnas_matriz_1)] for j in range(filas_matriz_1)]

print(resta)