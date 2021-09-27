from generadores import *
import Pruebas_uniformidad as prueba
import Pruebas_independencia as pruebaI
from os import system
contador = True
contador2 = True
contador3 = True

def probar_generadores():
    while True:
        print("############################# Bienvenido al menu de generadores ###############################")
        print("")
        print("1.Generador lineal congruente")
        print("2.Generador estandar minimo")
        print("3.Generador de python")
        print("4.Volver")
        print("")
        print("############################################################")
        Puntero_Interno = int(input("Eliga una opcion:"))
        while (Puntero_Interno > 4 or Puntero_Interno < 1):
            Puntero_Interno = int(input("Eliga una opcion:"))
        if Puntero_Interno == 1:
            system("cls")
            print("######################## Bienvenido al  generador lineal congruente ####################################")
            print("")
            datos = int(input("ingrese los datos que desea generar: "))
            generadorlincong(datos)
            VerDatosGenerados(returnDatos())
            print("1.Mostrar recurrencia")
            print("2.Volver")
            print("############################################################")
            Puntero_Interno2 = int(input("Eliga una opcion:"))
            while (Puntero_Interno2 > 2 or Puntero_Interno2 < 1):
                Puntero_Interno2 = int(input("Eliga una opcion:"))
            while 1:
                system("cls")
                if Puntero_Interno2 == 1:
                    print("Recurrencia lineal congruente")
                    VerDatosGenerados(returnRecurrrencias())
                    ReiniciarListas(returnRecurrrencias())
                    ReiniciarListas(returnDatos())
                    break
                elif Puntero_Interno2 == 2:
                    ReiniciarListas(returnRecurrrencias())
                    ReiniciarListas(returnDatos())
                    break
        elif Puntero_Interno == 2:
            system("cls")
            print("######################## Bienvenido al generador de estandar minimo ####################################")
            print("")
            datos = int(input("ingrese los datos que desea generar: "))
            print("")
            generadorestmin(datos)
            VerDatosGenerados(returnDatos())
            print("")
            print("1.Mostrar recurrencia")
            print("2.Volver")
            print("")
            print("############################################################")
            Puntero_Interno2 = int(input("Eliga una opcion:"))
            while (Puntero_Interno2 > 2 or Puntero_Interno2 < 1):
                Puntero_Interno2 = int(input("Eliga una opcion:"))
            while 1:
                system("cls")
                if Puntero_Interno2 == 1:
                    print("")
                    print("Mostrar recurrencia del estandar minimo")
                    VerDatosGenerados(returnRecurrrencias())
                    ReiniciarListas(returnRecurrrencias())
                    ReiniciarListas(returnDatos())
                    break
                elif Puntero_Interno2 == 2:
                    ReiniciarListas(returnRecurrrencias())
                    ReiniciarListas(returnDatos())
                    break
        elif Puntero_Interno == 3:
            system("cls")
            print("######################## Bienvenido al  generador Python ####################################")
            print("")
            datos = int(input("ingrese los datos que desea generar: "))
            generadorPython(datos)
            VerDatosGenerados(returnDatos())
            print("")
            print("1.Mostrar recurrencia")
            print("2.Volver")
            print("############################################################")
            Puntero_Interno2 = int(input("Eliga una opcion:"))
            while (Puntero_Interno2 > 2 or Puntero_Interno2 < 1):
                Puntero_Interno2 = int(input("Eliga una opcion:"))
            while 1:
                system("cls")
                if Puntero_Interno2 == 1:
                    print("Recurrencia lineal congruente")
                    VerDatosGenerados(returnRecurrrencias())
                    ReiniciarListas(returnRecurrrencias())
                    ReiniciarListas(returnDatos())
                    break
                elif Puntero_Interno2 == 2:
                    ReiniciarListas(returnRecurrrencias())
                    ReiniciarListas(returnDatos())
                    break
        elif Puntero_Interno == 4:
            system("cls")
            ReiniciarListas(returnRecurrrencias())
            ReiniciarListas(returnDatos())
            break

def menuUniformidad():
    while 1:
        system("cls")
        print("Se corre con 1000 datos generados y con 9 grados de libertad")
        print("############################# Bienvenido al menu de pruebas de uniformidad e independencia ###############################")
        print("\n")
        print("1.Generador lineal congruente")
        print("2.Generador estandar minimo")
        print("3.Generador de python")
        print("4.Volver")
        print("############################################################")
        Puntero_Interno = int(input("Porfavor seleccione un generador:"))
        while (Puntero_Interno > 4 or Puntero_Interno < 1):
            Puntero_Interno = int(input("Porfavor seleccione un generador:"))
        if Puntero_Interno == 1:
            system("cls")
            Prubas_Uniformidad_independencia(1)
        if Puntero_Interno == 2:
            system("cls")
            Prubas_Uniformidad_independencia(2)
        if Puntero_Interno == 3:
            system("cls")
            Prubas_Uniformidad_independencia(3)
        if Puntero_Interno == 4:
            system("cls")
            break

def Prubas_Uniformidad_independencia(Puntero_Interno):
    if Puntero_Interno == 1:
        system("cls")
        while 1:
            print("######################## Bienvenido al menu de pruebas de uniformidad del generador lineal congruente ####################################")
            print("1.Prueba de x2")
            print("2.Prueba kolmogorov")
            print("3.Volver")
            print("############################################################")
            print("")
            Puntero_Interno2 = int(input("Porfavor seleccione una prueba:"))
            print("")
            while (Puntero_Interno2 > 3 or Puntero_Interno2 < 1):
                Puntero_Interno2 = int(input("Porfavor seleccione una prueba:"))
            if Puntero_Interno2 == 1:
                system("cls")
                print("\n")
                print("/////////PRUEBA DE CHI CUADRADO ////////////////")
                prueba.PruebaChiCuadrado(1)
                print("\n")
                while 1:
                    print("######################## Bienvenido al menu de las pruebas de independencia del generador lineal congruente ####################################")
                    print("Que desea hacer ahora?")
                    print("1.Pruebas de Independencia")
                    print("2.volver")
                    print("######################## ############################################## ####################################")
                    Puntero_Interno3 = int(input("Escoga una opcion:"))
                    print("")
                    while (Puntero_Interno3 > 2 or Puntero_Interno3 < 1 ):
                        Puntero_Interno3 = int(input("Escoga una opcion:"))
                    if Puntero_Interno3 == 1:
                        print("######################## Bienvenido a las pruebas de independencia del generador lineal congruente ####################################")
                        print("1.Prueba de corrida")
                        print("2.Prueba de serie")
                        print("3.Prueba de poker")
                        print("4.Volver")
                        print("##############################################################################################################")
                        Puntero_Interno4 = int(input("Porfavor seleccione una prueba:"))
                        print("")
                        while (Puntero_Interno4 > 4 or Puntero_Interno4 < 1 ):
                            Puntero_Interno4 = int(input("Porfavor seleccione una prueba:"))
                        while 1:
                            if Puntero_Interno4 == 1:
                                print("")
                                print("///////////////////// Prueba de corrida ///////////////////" )
                                print("")
                                pruebaI.PruebaCorridas(returnRecurrrencias(),1000)
                                break
                            elif Puntero_Interno4 == 2:
                                print("")
                                print("///////////////////// Prueba de series ///////////////////" )
                                print("")
                                pruebaI.pruebaSeries(returnRecurrrencias())
                                break
                            elif  Puntero_Interno4 == 3:
                                print("")
                                print("///////////////////// Prueba de poker ///////////////////" )
                                print("")
                                pruebaI.pruebaPoker(returnRecurrrencias())
                                break
                            elif Puntero_Interno4 == 4:
                                break
                    elif Puntero_Interno3 == 2:
                        system("cls")
                        ReiniciarArreglos(returnTabla())
                        ReiniciarListas(returnDatos())
                        ReiniciarListas(returnRecurrrencias())
                        break
            elif Puntero_Interno2 == 2:
                #Prueba de kolmogorov aqui
                system("cls")
                print("\n")
                print("/////////PRUEBA DE KOLMOGOROV////////////////")
                prueba.PruebaKolmogorov(1)
                print("\n")
                while 1:
                    print("######################## Bienvenido al menu de las pruebas de independencia del generador lineal congruente ####################################")
                    print("Que desea hacer ahora?")
                    print("1.Pruebas de Independencia")
                    print("2.volver")
                    print("######################## ############################################## ####################################")
                    Puntero_Interno3 = int(input("Escoga una opcion:"))
                    print("")
                    while (Puntero_Interno3 > 2 or Puntero_Interno3 < 1 ):
                        Puntero_Interno3 = int(input("Escoga una opcion:"))
                    if Puntero_Interno3 == 1:
                        print("######################## Bienvenido a las pruebas de independencia ####################################")
                        print("1.Prueba de corrida")
                        print("2.Prueba de serie")
                        print("3.Prueba de poker")
                        print("4.Volver")
                        print("##############################################################################################################")
                        Puntero_Interno4 = int(input("Porfavor seleccione una prueba:"))
                        print("")
                        while (Puntero_Interno4 > 4 or Puntero_Interno4 < 1 ):
                            Puntero_Interno4 = int(input("Porfavor seleccione una prueba:"))
                        while 1:

                            if Puntero_Interno4 == 1:
                                print("")
                                print("///////////////////// Prueba de corrida ///////////////////" )
                                print("")
                                pruebaI.PruebaCorridas(returnRecurrrencias(),1000)
                                break
                            elif Puntero_Interno4 == 2:
                                print("")
                                print("///////////////////// Prueba de series ///////////////////" )
                                print("")
                                pruebaI.pruebaSeries(returnRecurrrencias())
                                break
                            elif  Puntero_Interno4 == 3:
                                print("")
                                print("///////////////////// Prueba de poker ///////////////////" )
                                print("")
                                pruebaI.pruebaPoker(returnRecurrrencias())
                                break
                            elif Puntero_Interno4 == 4:
                                break
                    elif Puntero_Interno3 == 2:
                        system("cls")
                        ReiniciarArreglos(returnTabla())
                        ReiniciarListas(returnDatos())
                        ReiniciarListas(returnRecurrrencias())
                        break
            elif Puntero_Interno2 == 3:
                system("cls")
                break
    elif Puntero_Interno == 2:
        system("cls")
        while 1:
            print("######################## Bienvenido al menu de las pruebas de uniformidad del generador de Estandar minimo ####################################")
            print("1.Prueba de x2")
            print("2.Prueba kolmogorov")
            print("3.Volver")
            print("############################################################")
            Puntero_Interno2 = int(input("Porfavor seleccione una prueba:"))
            print("")
            while (Puntero_Interno2 > 3 or Puntero_Interno2 < 1):
                Puntero_Interno2 = int(input("Porfavor seleccione una prueba:"))
            if Puntero_Interno2 == 1:
                system("cls")
                print("\n")
                print("/////////PRUEBA DE chi cuadrado////////////////")
                prueba.PruebaChiCuadrado(2)
                print("\n")
                while 1:
                    print("######################## Bienvenido al menu de las pruebas de independencia del generador de Estandar minimo ####################################")
                    print("Que desea hacer ahora?")
                    print("1.Pruebas de Independencia")
                    print("2.volver")
                    print("######################## ############################################## ####################################")
                    Puntero_Interno3 = int(input("Escoga una opcion:"))
                    print("")
                    while (Puntero_Interno3 > 2 or Puntero_Interno3 < 1 ):
                        Puntero_Interno3 = int(input("Escoga una opcion:"))
                    if Puntero_Interno3 == 1:
                        print("######################## Bienvenido a las pruebas de independencia ####################################")
                        print("1.Prueba de corrida")
                        print("2.Prueba de serie")
                        print("3.Prueba de poker")
                        print("4.Volver")
                        print("##############################################################################################################")
                        Puntero_Interno4 = int(input("Porfavor seleccione una prueba:"))
                        print("")
                        while (Puntero_Interno4 > 4 or Puntero_Interno4 < 1 ):
                            Puntero_Interno4 = int(input("Porfavor seleccione una prueba:"))
                        while 1:
                            if Puntero_Interno4 == 1:
                                print("")
                                print("///////////////////// Prueba de corrida ///////////////////" )
                                print("")
                                pruebaI.PruebaCorridas(returnRecurrrencias(),1000)
                                break
                            elif Puntero_Interno4 == 2:
                                print("")
                                print("///////////////////// Prueba de series ///////////////////" )
                                print("")
                                pruebaI.pruebaSeries(returnRecurrrencias())
                                break
                            elif  Puntero_Interno4 == 3:
                                print("")
                                print("///////////////////// Prueba de poker ///////////////////" )
                                print("")
                                pruebaI.pruebaPoker(returnRecurrrencias())
                                break
                            elif Puntero_Interno4 == 4:
                                break
                    elif Puntero_Interno3 == 2:
                        system("cls")
                        ReiniciarArreglos(returnTabla())
                        ReiniciarListas(returnDatos())
                        ReiniciarListas(returnRecurrrencias())
                        break
            elif Puntero_Interno2 == 2:
                system("cls")
                print("/////////PRUEBA DE KOLMOGOROV////////////////")
                prueba.PruebaKolmogorov(2)
                while 1:
                    print("\n")
                    print("\n")
                    print("######################## Bienvenido al menu de las pruebas de independencia del generador de estandar minimo ####################################")
                    print("Que desea hacer ahora?")
                    print("1.Pruebas de Independencia")
                    print("2.volver")
                    print("######################## ############################################## ####################################")
                    Puntero_Interno3 = int(input("Escoga una opcion:"))
                    print("")
                    while (Puntero_Interno3 > 2 or Puntero_Interno3 < 1 ):
                        Puntero_Interno3 = int(input("Escoga una opcion:"))
                    if Puntero_Interno3 == 1:
                        print("######################## Bienvenido a las pruebas de independencia ####################################")
                        print("1.Prueba de corrida")
                        print("2.Prueba de serie")
                        print("3.Prueba de poker")
                        print("4.Volver")
                        print("##############################################################################################################")
                        Puntero_Interno4 = int(input("Porfavor seleccione una prueba:"))
                        print("")
                        while (Puntero_Interno4 > 4 or Puntero_Interno4 < 1 ):
                            Puntero_Interno4 = int(input("Porfavor seleccione una prueba:"))
                        while 1:
                            if Puntero_Interno4 == 1:
                                print("")
                                print("///////////////////// Prueba de corrida ///////////////////" )
                                print("")
                                pruebaI.PruebaCorridas(returnRecurrrencias(),1000)
                                break
                            elif Puntero_Interno4 == 2:
                                print("")
                                print("///////////////////// Prueba de series ///////////////////" )
                                print("")
                                pruebaI.pruebaSeries(returnRecurrrencias())
                                break
                            elif  Puntero_Interno4 == 3:
                                print("")
                                print("///////////////////// Prueba de poker ///////////////////" )
                                print("")
                                pruebaI.pruebaPoker(returnRecurrrencias())
                                break
                            elif Puntero_Interno4 == 4:
                                break
                    elif Puntero_Interno3 == 2:
                        system("cls")
                        ReiniciarArreglos(returnTabla())
                        ReiniciarListas(returnDatos())
                        ReiniciarListas(returnRecurrrencias())
                        break
            elif Puntero_Interno2 == 3:
                system("cls")
                break
    if Puntero_Interno == 3:
        system("cls")
        while 1:
            print("######################## Bienvenido al menu de las pruebas de uniformidad del generador de Python ####################################")
            print("1.Prueba de x2")
            print("2.Prueba kolmogorov")
            print("3.Volver")
            print("############################################################")
            Puntero_Interno2 = int(input("Porfavor seleccione una prueba:"))
            print("")
            while (Puntero_Interno2 > 3 or Puntero_Interno2 < 1):
                Puntero_Interno2 = int(input("Porfavor seleccione una prueba:"))
            if Puntero_Interno2 == 1:
                system("cls")
                print("\n")
                print("/////////PRUEBA DE CHI CUADRADO ////////////////")
                prueba.PruebaChiCuadrado(3)
                print("\n")
                while 1:
                    print("######################## Bienvenido al menu de las pruebas de independencia del generador de Python ####################################")
                    print("Que desea hacer ahora?")
                    print("1.Pruebas de Independencia")
                    print("2.volver")
                    print("######################## ############################################## ####################################")
                    Puntero_Interno3 = int(input("Escoga una opcion:"))
                    print("")
                    while (Puntero_Interno3 > 2 or Puntero_Interno3 < 1 ):
                        Puntero_Interno3 = int(input("Escoga una opcion:"))
                    if Puntero_Interno3 == 1:
                        print("######################## Bienvenido a las pruebas de independencia ####################################")
                        print("1.Prueba de corrida")
                        print("2.Prueba de serie")
                        print("3.Prueba de poker")
                        print("4.Volver")
                        print("##############################################################################################################")
                        Puntero_Interno4 = int(input("Porfavor seleccione una prueba:"))
                        print("")
                        while (Puntero_Interno4 > 4 or Puntero_Interno4 < 1 ):
                            Puntero_Interno4 = int(input("Porfavor seleccione una prueba:"))
                        while 1:
                            if Puntero_Interno4 == 1:
                                print("")
                                print("///////////////////// Prueba de corrida ///////////////////" )
                                print("")
                                pruebaI.PruebaCorridas(returnRecurrrencias(),1000)
                                break
                            elif Puntero_Interno4 == 2:
                                print("")
                                print("///////////////////// Prueba de series ///////////////////" )
                                print("")
                                pruebaI.pruebaSeries(returnRecurrrencias())
                                break
                            elif  Puntero_Interno4 == 3:
                                print("")
                                print("///////////////////// Prueba de poker ///////////////////" )
                                print("")
                                pruebaI.pruebaPoker(returnRecurrrencias())
                                break
                            elif Puntero_Interno4 == 4:
                                break
                    elif Puntero_Interno3 == 2:
                        system("cls")
                        ReiniciarArreglos(returnTabla())
                        ReiniciarListas(returnDatos())
                        ReiniciarListas(returnRecurrrencias())
                        break
            elif Puntero_Interno2 == 2:
                #Prueba de kolmogorov aqui
                system("cls")
                print("\n")
                print("/////////PRUEBA DE KOLMOGOROV////////////////")
                prueba.PruebaKolmogorov(3)
                print("\n")
                while 1:
                    print("######################## Bienvenido al menu de las pruebas de independencia del generador de Python ####################################")
                    print("Que desea hacer ahora?")
                    print("1.Pruebas de Independencia")
                    print("2.volver")
                    print("######################## ############################################## ####################################")
                    Puntero_Interno3 = int(input("Escoga una opcion:"))
                    print("")
                    while (Puntero_Interno3 > 2 or Puntero_Interno3 < 1 ):
                        Puntero_Interno3 = int(input("Escoga una opcion:"))
                    if Puntero_Interno3 == 1:
                        print("######################## Bienvenido a las pruebas de independencia ####################################")
                        print("1.Prueba de corrida")
                        print("2.Prueba de serie")
                        print("3.Prueba de poker")
                        print("4.Volver")
                        print("##############################################################################################################")
                        Puntero_Interno4 = int(input("Porfavor seleccione una prueba:"))
                        print("")
                        while (Puntero_Interno4 > 4 or Puntero_Interno4 < 1 ):
                            Puntero_Interno4 = int(input("Porfavor seleccione una prueba:"))
                        while 1:

                            if Puntero_Interno4 == 1:
                                print("")
                                print("///////////////////// Prueba de corrida ///////////////////" )
                                print("")
                                pruebaI.PruebaCorridas(returnRecurrrencias(),1000)
                                break
                            elif Puntero_Interno4 == 2:
                                print("")
                                print("///////////////////// Prueba de series ///////////////////" )
                                print("")
                                pruebaI.pruebaSeries(returnRecurrrencias())
                                break
                            elif  Puntero_Interno4 == 3:
                                print("")
                                print("///////////////////// Prueba de poker ///////////////////" )
                                print("")
                                pruebaI.pruebaPoker(returnRecurrrencias())
                                break
                            elif Puntero_Interno4 == 4:
                                break
                    elif Puntero_Interno3 == 2:
                        system("cls")
                        ReiniciarArreglos(returnTabla())
                        ReiniciarListas(returnDatos())
                        ReiniciarListas(returnRecurrrencias())
                        break
            elif Puntero_Interno2 == 3:
                system("cls")
                break

def menuPrincipal():
    while contador == True:
        system("cls")
        print("############################ MENU ###################################")
        print("Bienvenido al menu de las pruebas de independencia y uniformidad")
        print("\n")
        print("1.Probar generadores")
        print("2.Pruebas de uniformidad e independencia")
        print("3.Salir")
        print("\n")
        Puntero_Menu = int(input("Eliga una opcion:"))
        print("")
        while (Puntero_Menu > 4 or Puntero_Menu < 1):
            Puntero_Menu = int(input("Eliga una numero entero entre 1 y 4 no es tan dificil:"))
        if Puntero_Menu == 1:
            system("cls")
            probar_generadores()
        elif Puntero_Menu == 2:
            system("cls")
            menuUniformidad()
        else:
            break
    print("##################### FIN DEL PROGRAMA ##############################")
