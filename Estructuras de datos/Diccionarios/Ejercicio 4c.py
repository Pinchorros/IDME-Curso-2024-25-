"""Escribir un programa que cree un diccionario simulando una cesta
 de la compra. El programa debe preguntar el artículo y su precio
y añadirlo al diccionario, hasta que el usuario decida terminar.
Después se debe mostrar por pantalla la lista de la compra y el coste
 total."""

# Importación de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:

compra = {} # Diccionario que la lista de la compra.
producto = "" # Nombre del artículo
precio = "" # Precio del artículo

# Programa principal:

system("cls") # Borra la pantalla.