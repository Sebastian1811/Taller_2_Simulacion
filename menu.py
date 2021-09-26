from generadores import *
import Pruebas_uniformidad as prueba
contador = True
contador2 = True
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
    while (Puntero_Menu > 4 or Puntero_Menu < 1):
        Puntero_Menu = int(input("Eliga una numero entero entre 1 y 4 no es tan dificil:"))
    if Puntero_Menu == 1:
        print("Usted selecciono el generador lineal congruente con las pruebas de uniformidad")
        print("1.Prueba del chi cuadrado")
        print("2.prueba de kolmogorov")
        Puntero_Interno = int(input("Eliga una opcion:"))
        while(Puntero_Interno > 2 or Puntero_Interno < 1):
            Puntero_Interno = int(input("Pon una opcion valida:"))
        if Puntero_Interno == 1:
            generadorlincong(1000)
            prueba.PruebaChiCuadrado(returnTabla(),returnN())
            ReiniciarArreglos(returnTabla())
        elif Puntero_Interno ==2:
            generadorlincong(1000)
            prueba.PruebaKolmogorov(returnTabla(),returnN())
            ReiniciarArreglos(returnTabla())
        print("Desea continuar?")
        print("Si?: presione 1")
        print("No?: presione 2")
        Continuar = int(input("Digite una de las 2 opciones:"))
        while(Continuar > 2 or Continuar < 1):
            Continuar = int(input("Digite una de las 2 opciones:"))
        if Continuar == 1:
            print("Reinicio")
        else:
            contador = False
    elif Puntero_Menu == 2:
        print("Usted selecciono el generador de estandar minimo con las pruebas de uniformidad")
        print("1.Prueba del chi cuadrado")
        print("2.prueba de kolmogorov")
        Puntero_Interno = int(input("Eliga una opcion:"))
        while(Puntero_Interno > 2 or Puntero_Interno < 1):
            Puntero_Interno = int(input("Pon una opcion valida:"))
        if Puntero_Interno == 1:
            generadorestmin()
            prueba.PruebaChiCuadrado(returnTabla(),returnN())
            ReiniciarTabla()
        elif Puntero_Interno ==2:
            generadorestmin()
            prueba.PruebaKolmogorov(returnTabla(),returnN())
            ReiniciarTabla()
        print("Desea continuar?")
        print("Si?: presione 1")
        print("No?: presione 2")
        Continuar = int(input("Digite una de las 2 opciones:"))
        while(Continuar > 2 or Continuar < 1):
            Continuar = int(input("Digite una de las 2 opciones:"))
        if Continuar == 1:
            print("Reinicio")
        else:
            contador = False
    elif Puntero_Menu == 3:
        print("")
    else:
        print("")
