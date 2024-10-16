"""(Estructura “elif”) Pide por teclado un valor entre 1 y 7 y debe
indicarnos por pantalla el día de la semana correspondiente."""

# Importación de librerías:

from os import system

# Declaración de variables:

numeroDia = 0 # Contendrá el número de orden del día de la semana.

# Programa principal:

system("cls")

numeroDia = int(input("Introduce el número del día de la semana: "))

if numeroDia == 1:
    print("Has introducido Lunes.")
elif numeroDia == 2:
    print("Has tecleado Martes.")
elif numeroDia == 3:
    print("Has tecleado Miércoles.")
elif numeroDia == 4:
    print("Has tecleado Jueves.")
elif numeroDia == 5:
    print("Has tecleado Viernes.")
elif numeroDia == 6:
    print("Has tecleado Sábado.")
elif numeroDia == 7:
    print("Has tecleado Domingo.")
else:
    print("Haz el favor de no ser tan gracioso e introducir un valor entre 1 y 7 :-P")

