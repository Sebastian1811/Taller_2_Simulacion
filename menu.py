from generadores import *
contador = True
while contador == True:

    print("############################ ANOTACIONES ###################################")
    print("Se implementaron los generadores lineal y congruente con 9 grados de libertad, se generaron 1000 numeros pseudoaleatorios por cada generador")

    print("############################ MENU ###################################")
    print("Bienvenido al menu de las pruebas de independencia y uniformidad")
    print("\n")
    print("1.Generador lineal congruente con pruebas de uniformidad")
    print("2.Generador de estandar minimo con pruebas de uniformidad")
    print("3.Generador lineal congruente con pruebas de independencia")
    print("4.Generador de estandar minimo con pruebas de independencia")
    print("\n")

    Puntero_Menu = int(input("Eliga una opcion:"))

    if Puntero_Menu == 1:
        print("Usted selecciono el generador lineal congruente con las pruebas de uniformidad")
        print("1.Prueba del chi cuadrado")
        print("2.prueba de kolmogorov")
        Puntero_Interno = int(input("Eliga una opcion:"))
        if Puntero_Interno == 1:
            print("1")
        else:
            print("Kolmogorov")
        print("Desea continuar?")
        print("Si?: presione 1")
        print("No?: presione 2")
        Continuar = int(input("Digite una de las 2 opciones:"))
        if Continuar == 1:
            print("Reinicio")
        else:
            contador = False
    elif Puntero_Menu == 2:
        print("Usted selecciono el generador de estandar minimo con las pruebas de uniformidad")
        generadorestmin()
    elif Puntero_Menu == 3:
        print("")
    else:
        print("")
