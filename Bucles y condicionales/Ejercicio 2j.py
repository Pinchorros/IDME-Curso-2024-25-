"""Pida por teclado números, hasta que introduzca el 0. Posteriormente debe
mostrar su suma y su producto.
"""
# Importanción de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:

numero = 1 # (Con decimales) Para pedir por teclado el valor con el que voy a operar.
suma = 0 # Para acumular los valores sumados del número pedido por teclado.
producto = 1 # Para acumular la multiplicación de los números.

# Programa principal:

system("cls")

while numero != 0:
    numero = float(input("Introduce el número a multiplicar y sumar (0 para terminar): "))
    suma = suma + numero
    if numero != 0:
        producto = producto * numero

print(f"La suma total de los números es {suma}")
print(f"La multiplicación total es {producto}")
