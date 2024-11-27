"""Programa que pedirá por teclado asignaturas con su calificación. Luego
 debe mostrar sólo las aprobadas (>5) y la media aritmética de todas
  las calificaciones. """

# Importación de librerías:
from os import system # Importo el comando "system" de la librería "os".

# Declaración de variables:

asignaturas = {} # Diccionario que contendrá los datos (nombre y nota)
nombreAsignatura = " " 
calificacion = 0 # Contendrá la nota entre 0 y 10 (con decimales).
sumaCalificaciones = 0 # Para calcular la media aritmética.

# Programa principal:

system("cls")
while nombreAsignatura != "": # Bucle para pedir las asignaturas
    nombreAsignatura = input("Teclea asignatura (ENTER para finalizar): ")
    if nombreAsignatura != "":
        calificacion = float(input("Introduce la calificación de la asignatura: "))
        asignaturas[nombreAsignatura] = calificacion
    print("") # Salto de línea para separar asignaturas.

for nombreAsignatura in asignaturas:
    if asignaturas[nombreAsignatura] >= 5:
        print(f"La asignatura {nombreAsignatura} está aprobada con un {asignaturas[nombreAsignatura]}")
    sumaCalificaciones = sumaCalificaciones + asignaturas[nombreAsignatura]

print("") # Salto de línea.
print(f"La media aritmética de {len(asignaturas)} asignaturas es {sumaCalificaciones/len(asignaturas)}")
