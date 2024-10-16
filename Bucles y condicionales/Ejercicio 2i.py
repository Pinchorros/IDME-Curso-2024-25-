"""" Que sume todos los números pares positivos, partiendo desde 0, hasta que la suma supere el valor
 de 1000. Posteriormente, debe mostrar en pantalla cuál es el valor de la suma y cuántos números
 se han sumado.
"""

# Importación de librerías:

from os import system

# Declaración de variables

suma = 0 # Donde voy a ir acumulando la suma de los números pares.
numero = 2 # Va a contener los números pares que voy a sumar.
contador = 0 # Cuenta la cantidad de números que he sumado.

# Programa principal:

system("cls") # Ejecuta el comando "cls" del sistema operativo MS Windows.

while suma <= 1000:
    suma += numero #suma = suma + numero 
    numero += 2 # Equivale a escribir numero = numero + 2.
    contador += 1

print(f"La suma total es {suma}.")
print(f"El número de valores sumados es {contador}")
print(f"El último número sumado es {numero}")

