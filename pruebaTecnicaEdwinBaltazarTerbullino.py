from collections import Counter
def ejercicio1(matriz):
    frecuencia = Counter(num for fila in matriz for num in fila)
    unicos = sum(1 for count in frecuencia.values() if count == 1)
    repetidos = len(frecuencia) - unicos
    return [unicos, repetidos]


def ejercicio2(n):
    pares = []
    for i in range(1, n // 2 + 1):
        pares.append((i, n - i))
    return pares

#Ejercicio 1
print("EJERCICIO 1 :")
matriz1 = [[2, 2], [2, 2]]
matriz2 = [[2, 1, 3], [4, 5, 2], [6, 6, 6]]
print(ejercicio1(matriz1))
print(ejercicio1(matriz2))
print("----------")
#Ejercicio 2
print("EJERCICIO 2 :")
n1 = 5
n2 = 10
print(ejercicio2(n1))  
print(ejercicio2(n2))  