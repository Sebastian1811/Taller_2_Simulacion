from generadores import *
import Pruebas_uniformidad as prueba
contador = True
contador2 = True
contador3 = True

def probar_generadores():
    while True:
        print("############################# Bienvenido al menu de generadores ###############################")
        print("")
        print("1.Generador lineal congruente")
        print("2.Generador estandar minimo")
        print("3.Volver")
        print("############################################################")
        Puntero_Interno = int(input("Eliga una opcion:"))
        while (Puntero_Interno > 3 or Puntero_Interno < 1):
            Puntero_Interno = int(input("Eliga una opcion:"))


        if Puntero_Interno == 1:
            print("######################## Bienvenido al menu del generador lineal congruente ####################################")
            print("1.Mostrar recurrencia")
            print("2.Volver")
            print("############################################################")
            Puntero_Interno2 = int(input("Eliga una opcion:"))
            while (Puntero_Interno2 > 2 or Puntero_Interno2 < 1):
                Puntero_Interno2 = int(input("Eliga una opcion:"))
            while 1:
                if Puntero_Interno2 == 1:
                    #Mostrar recurrencia lc
                    print("Recurrencia lineal congruente")
                    break
                elif Puntero_Interno2 == 2:
                    break
        elif Puntero_Interno == 2:
            print("######################## Bienvenido al menu del generador de estandar minimo ####################################")
            print("1.Mostrar recurrencia")
            print("2.Volver")
            print("############################################################")
            Puntero_Interno2 = int(input("Eliga una opcion:"))
            while (Puntero_Interno2 > 2 or Puntero_Interno2 < 1):
                Puntero_Interno2 = int(input("Eliga una opcion:"))
            while 1:
                if Puntero_Interno2 == 1:
                    #Mostrar recurrencia em
                    print("Mostrar recurrencia del estandar minimo")
                    break
                elif Puntero_Interno2 == 2:
                    break
        elif Puntero_Interno == 3:
            break




while contador == True:
    print("############################ MENU ###################################")
    print("Bienvenido al menu de las pruebas de independencia y uniformidad")
    print("\n")
    print("1.Probar generadores")
    print("2.Generador de estandar minimo con pruebas de uniformidad")
    print("3.Generador lineal congruente con pruebas de independencia")
    print("4.Generador de estandar minimo con pruebas de independencia")
    print("\n")

    Puntero_Menu = int(input("Eliga una opcion:"))
    while (Puntero_Menu > 4 or Puntero_Menu < 1):
        Puntero_Menu = int(input("Eliga una numero entero entre 1 y 4 no es tan dificil:"))
    if Puntero_Menu == 1:
        probar_generadores()
"""
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
"""
