import random

#Se pide al usuario que ingrese las filas y columnas de la primera matriz
filas_matriz_1 = int(input("Ingrese la cantidad de filas de la primera matriz: "))
columnas_matriz_1 = int(input("Ingrese la cantidad de columnas de la primera matriz: "))

#Se pide al usuario que ingrese las filas y columnas de la segunda matriz
filas_matriz_2 = int(input("Ingrese la cantidad de filas de la segunda matriz: "))
columnas_matriz_2 = int(input("Ingrese la cantidad de columnas de la segunda matriz: "))

#Se crea la matriz con los datos entregados por consola
#Se utiliza el random para que los elementos de la matriz sean aleatorias entre 0 y 5
matriz_1 = [[random.randint(0, 5) for i in range(columnas_matriz_1)] for j in range(filas_matriz_1)]
matriz_2 = [[random.randint(0, 5) for i in range(columnas_matriz_2)] for j in range(filas_matriz_2)]

#Se imprimen la primera matriz
print("La matriz uno es")
for i in range(columnas_matriz_1):
    for j in range(filas_matriz_1):
        print(matriz_1[i][j])

print()

#Se imprime la segunda matriz
print("La matriz dos es")
for i in range(columnas_matriz_2):
    for j in range(filas_matriz_2):
        print(matriz_2[i][j])

print()

#Aqui se suma la matriz uno con la matriz dos y luego se imprime el resultante
suma = [[matriz_1[i][j] + matriz_2[i][j] for i in range(columnas_matriz_1)] for j in range(filas_matriz_1)]

print(suma)

#Se pide ingresar los datos de la tercera matriz
filas_matriz_3 = int(input("Ingrese la cantidad de filas de la tercera matriz: "))
columnas_matriz_3 = int(input("Ingrese la cantidad de columnas de la tercera matriz: "))

matriz_3 = [[random.randint(0, 5) for i in range(columnas_matriz_3)] for j in range(filas_matriz_3)]

#Se imprimen la tercera matriz
print("La matriz tres es")
for i in range(columnas_matriz_3):
    for j in range(filas_matriz_3):
        print(matriz_3[i][j])

print()

#Aqui el resultado de la suma de las primeras dos matrices se restara a una tercera matriz creada previamente
resta = [[suma[i][j]-matriz_3[i][j]] for i in range(columnas_matriz_1) for j in range(filas_matriz_1)]

print(resta)