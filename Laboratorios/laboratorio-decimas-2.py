import random

#Se pide al usuario que ingrese las filas y columnas de la primera matriz
filas_matriz_1 = int(input("Ingrese la cantidad de filas de la primera matriz: "))
columnas_matriz_1 = int(input("Ingrese la cantidad de columnas de la primera matriz: "))

#Se pide al usuario que ingrese las filas y columnas de la segunda matriz
filas_matriz_2 = int(input("Ingrese la cantidad de filas de la segunda matriz: "))
columnas_matriz_2 = int(input("Ingrese la cantidad de columnas de la segunda matriz: "))

#Se agregan datos aleatorios a las matrices y se imprimen
matriz_1 = [[random.randint(1, 5) for i in range(columnas_matriz_1)] for j in range(filas_matriz_1)]
matriz_2 = [[random.randint(1, 5) for i in range(columnas_matriz_2)] for j in range(filas_matriz_2)]

print(matriz_1)
print(matriz_2)

#Se suma la matriz 1 con la matriz 2 y imprime el resultado
suma = [[matriz_1[i][j] + matriz_2[i][j] for i in range(columnas_matriz_1)] for j in range(filas_matriz_1)]

print(suma)

#Se resta la matriz 1 con la matriz 2 y imprime el resultado
resta = [[matriz_1[i][j] - matriz_2[i][j] for i in range(columnas_matriz_1)] for j in range(filas_matriz_1)]

print(resta)