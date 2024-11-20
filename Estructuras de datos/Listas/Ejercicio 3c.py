""" Introduciremos por teclado una matriz de 2 x 2, y nos 
devolverá el valor de su determinante.
"""

# Importación de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:
matriz = [[0, 0],[0, 0]] # La lista que contendrá todos los elementos de la matriz
determinante = 0 # Contiene el valor de la solución.
fila = 0
columna = 0

# Programa principal:

system("cls")

for fila in range(0,2): # Recuerda que range llega hasta un valor por debajo del 2º parámetro.
    for columna in range(0,2):
        matriz[fila][columna] = float(input(f"Teclea la posición fila {fila}, columna {columna}: "))

determinante = matriz[0][0] * matriz[1][1] - matriz[1][0] * matriz[0][1]

print(f"La solución del deteminante de la matriz es: {determinante}.")
