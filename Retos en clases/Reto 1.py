#Reto 3

palabra = input("Ingrese una palabra: ")
vocales = ["a", "e", "i", "o", "u"]
#count: Recibe un elemento como argumento, y cuenta la cantidad de veces que aparece en la lista.
contador = [palabra.count(v) for v in vocales] 

for i in range(len(vocales)):
    print(f"la vocal {vocales[i]} aparece {contador[i]}")
