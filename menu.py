from generadores import *  

print("############################ MENU ###################################")
print("Se implementaron los generadores lineal y congruente con 9 grados de libertad, se generaron 1000 numeros pseudoaleatorios por cada generador")

Puntero_Menu = int(input("Eliga una opcion:"))

if Puntero_Menu == 1:
    print("Usted selecciono el generador lineal congruente con las pruebas de uniformidad")
    generadorlincong()
elif Puntero_Menu == 2:
    print("")
elif Puntero_Menu == 3:
    print("")
else:
    print("")
