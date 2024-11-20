""" Introduciremos por teclado una matriz de 2 x 2, y nos 
devolverá el valor de su determinante.
"""

# Importación de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:
matriz = [[0, 0],[0, 0]] # La lista que contendrá todos los elementos de la matriz
determinante = 0 # Contiene el valor de la solución.

# Programa principal:

system("cls")

matriz[0][0] = float(input("Teclea la posición superior izquierda de la matriz: "))
matriz[0][1] = float(input("Teclea la posición superior derecha de la matriz: "))
matriz[1][0] = float(input("Teclea la posición inferior izquierda de la matriz: "))
matriz[1][1] = float(input("Teclea la posición inferior derecha de la matriz: "))
determinante = matriz[0][0] * matriz[1][1] - matriz[1][0] * matriz[0][1]

print(f"La solución del deteminante de la matriz es: {determinante}.")
