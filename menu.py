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
        print("generador de python")
        print("3.Volver")
        print("")
        print("############################################################")
        Puntero_Interno = int(input("Eliga una opcion:"))
        while (Puntero_Interno > 3 or Puntero_Interno < 1):
            Puntero_Interno = int(input("Eliga una opcion:"))
        if Puntero_Interno == 1:
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
                if Puntero_Interno2 == 1:
                    #Mostrar recurrencia lc
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
                if Puntero_Interno2 == 1:
                    #Mostrar recurrencia em
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
            break

def menuUniformidad():
    while 1:
        print("Se corre con 1000 datos generados y con 9 grados de libertad")
        print("############################# Bienvenido al menu de pruebas de uniformidad ###############################")
        print("\n")
        print("1.Generador lineal congruente")
        print("2.Generador estandar minimo")
        print("3.Volver")
        print("############################################################")
        Puntero_Interno = int(input("Elija una opcion:"))
        while (Puntero_Interno > 3 or Puntero_Interno < 1):
            Puntero_Interno = int(input("Eliga una opcion:"))
        if Puntero_Interno == 1:
            Prubas_Uniformidad_independencia(1)
        if Puntero_Interno == 2:
            Prubas_Uniformidad_independencia(2)
        if Puntero_Interno == 3:
            break

def Prubas_Uniformidad_independencia(Puntero_Interno):

    if Puntero_Interno == 1:
        while 1:
            print("######################## Bienvenido al menu del generador lineal congruente ####################################")
            print("1.Prueba de x2")
            print("2.Prueba kolmogorov")
            print("3.Volver")
            print("############################################################")
            Puntero_Interno2 = int(input("Eliga una opcion:"))
            while (Puntero_Interno2 > 3 or Puntero_Interno2 < 1):
                Puntero_Interno2 = int(input("Eliga una opcion:"))

            if Puntero_Interno2 == 1:
                #Prueba del chi cuadrado aqui
                while 1:
                    print("\n")
                    print("/////////PRUEBA DE CHI CUADRADO ////////////////")
                    #generadorlincong(1000)
                    prueba.PruebaChiCuadrado(1)
                    print("\n")
                    print("######################## Bienvenido al menu de las pruebas de independencia ####################################")
                    print("Que desea hacer ahora?")
                    print("1.Pruebas de Independencia")
                    print("2.volver")
                    print("######################## ############################################## ####################################")
                    Puntero_Interno3 = int(input("Escoga una opcion:"))
                    while (Puntero_Interno3 > 2 or Puntero_Interno3 < 1 ):
                        Puntero_Interno3 = int(input("Escoga una opcion:"))
                    if Puntero_Interno3 == 1:
                        print("######################## Bienvenido al menu de las pruebas de independencia ####################################")
                        print("1.Prueba de corrida")
                        print("2.Prueba de serie")
                        print("3.Prueba de poker")
                        print("4.Volver")
                        print("##############################################################################################################")
                        Puntero_Interno4 = int(input("eliga una opcion:"))
                        while (Puntero_Interno4 > 4 or Puntero_Interno4 < 1 ):
                            Puntero_Interno4 = int(input("Escoga una opcion:"))
                        while 1:
                            if Puntero_Interno4 == 1:
                                #Mostrar Prueba de corrida aqui
                                print("Mostrar prueba de corrida")
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                            elif Puntero_Interno4 == 2:
                                #Mostrar prueba de serie aqui
                                print("Prueba de serie")
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                            elif  Puntero_Interno4 == 3:
                                #Mostrar prueba de poker aqui
                                print("Prueba de poker")
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                            elif Puntero_Interno4 == 4:
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                    elif Puntero_Interno3 == 2:
                        ReiniciarArreglos(returnTabla())
                        ReiniciarListas(returnDatos())
                        ReiniciarListas(returnRecurrrencias())
                        break
            elif Puntero_Interno2 == 2:
                #Prueba de kolmogorov aqui
                while 1:
                    print("\n")
                    print("/////////PRUEBA DE KOLMOGOROV////////////////")
                    prueba.PruebaKolmogorov(1)
                    print("\n")
                    print("######################## Bienvenido al menu de las pruebas de independencia ####################################")
                    print("Que desea hacer ahora?")
                    print("1.Pruebas de Independencia")
                    print("2.volver")
                    print("######################## ############################################## ####################################")
                    Puntero_Interno3 = int(input("Escoga una opcion:"))
                    while (Puntero_Interno3 > 2 or Puntero_Interno3 < 1 ):
                        Puntero_Interno3 = int(input("Escoga una opcion:"))
                    if Puntero_Interno3 == 1:
                        print("######################## Bienvenido al menu de las pruebas de independencia ####################################")
                        print("1.Prueba de corrida")
                        print("2.Prueba de serie")
                        print("3.Prueba de poker")
                        print("4.Volver")
                        print("##############################################################################################################")
                        Puntero_Interno4 = int(input("eliga una opcion:"))
                        while (Puntero_Interno4 > 4 or Puntero_Interno4 < 1 ):
                            Puntero_Interno4 = int(input("Escoga una opcion:"))
                        while 1:
                            if Puntero_Interno4 == 1:
                                #Mostrar Prueba de corrida aqui
                                print("Mostrar prueba de corrida")
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                            elif Puntero_Interno4 == 2:
                                #Mostrar prueba de serie aqui
                                print("Prueba de serie")
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                            elif  Puntero_Interno4 == 3:
                                #Mostrar prueba de poker aqui
                                print("Prueba de poker")
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                            elif Puntero_Interno4 == 4:
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                    elif Puntero_Interno3 == 2:
                        ReiniciarArreglos(returnTabla())
                        ReiniciarListas(returnDatos())
                        ReiniciarListas(returnRecurrrencias())
                        break
            elif Puntero_Interno2 == 3:
                break
    elif Puntero_Interno == 2:
        while 1:
            print("######################## Bienvenido al menu del generador Estandar minimo ####################################")
            print("1.Prueba de x2")
            print("2.Prueba kolmogorov")
            print("3.Volver")
            print("############################################################")
            Puntero_Interno2 = int(input("Eliga una opcion:"))
            while (Puntero_Interno2 > 3 or Puntero_Interno2 < 1):
                Puntero_Interno2 = int(input("Eliga una opcion:"))

            if Puntero_Interno2 == 1:
                #Prueba del chi cuadrado aqui
                while 1:
                    print("\n")
                    print("/////////PRUEBA DE chi cuadrado////////////////")
                    prueba.PruebaChiCuadrado(2)
                    print("\n")
                    print("######################## Bienvenido al menu de las pruebas de independencia ####################################")
                    print("Que desea hacer ahora?")
                    print("1.Pruebas de Independencia")
                    print("2.volver")
                    print("######################## ############################################## ####################################")
                    Puntero_Interno3 = int(input("Escoga una opcion:"))
                    while (Puntero_Interno3 > 2 or Puntero_Interno3 < 1 ):
                        Puntero_Interno3 = int(input("Escoga una opcion:"))
                    if Puntero_Interno3 == 1:
                        print("######################## Bienvenido al menu de las pruebas de independencia ####################################")
                        print("1.Prueba de corrida")
                        print("2.Prueba de serie")
                        print("3.Prueba de poker")
                        print("4.Volver")
                        print("##############################################################################################################")
                        Puntero_Interno4 = int(input("eliga una opcion:"))
                        while (Puntero_Interno4 > 4 or Puntero_Interno4 < 1 ):
                            Puntero_Interno4 = int(input("Escoga una opcion:"))
                        while 1:
                            if Puntero_Interno4 == 1:
                                #Mostrar Prueba de corrida aqui
                                print("Mostrar prueba de corrida")
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                            elif Puntero_Interno4 == 2:
                                #Mostrar prueba de serie aqui
                                print("Prueba de serie")
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                            elif  Puntero_Interno4 == 3:
                                #Mostrar prueba de poker aqui
                                print("Prueba de poker")
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                            elif Puntero_Interno4 == 4:
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                    elif Puntero_Interno3 == 2:
                        ReiniciarArreglos(returnTabla())
                        ReiniciarListas(returnDatos())
                        ReiniciarListas(returnRecurrrencias())
                        break
            elif Puntero_Interno2 == 2:
                #Prueba de kolmogorov aqui
                while 1:
                    print("\n")
                    print("/////////PRUEBA DE KOLMOGOROV////////////////")
                    prueba.PruebaKolmogorov(2)
                    print("\n")
                    print("######################## Bienvenido al menu de las pruebas de independencia ####################################")
                    print("Que desea hacer ahora?")
                    print("1.Pruebas de Independencia")
                    print("2.volver")
                    print("######################## ############################################## ####################################")
                    Puntero_Interno3 = int(input("Escoga una opcion:"))
                    while (Puntero_Interno3 > 2 or Puntero_Interno3 < 1 ):
                        Puntero_Interno3 = int(input("Escoga una opcion:"))
                    if Puntero_Interno3 == 1:
                        print("######################## Bienvenido al menu de las pruebas de independencia ####################################")
                        print("1.Prueba de corrida")
                        print("2.Prueba de serie")
                        print("3.Prueba de poker")
                        print("4.Volver")
                        print("##############################################################################################################")
                        Puntero_Interno4 = int(input("eliga una opcion:"))
                        while (Puntero_Interno4 > 4 or Puntero_Interno4 < 1 ):
                            Puntero_Interno4 = int(input("Escoga una opcion:"))
                        while 1:
                            if Puntero_Interno4 == 1:
                                #Mostrar Prueba de corrida aqui
                                print("Mostrar prueba de corrida")
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                            elif Puntero_Interno4 == 2:
                                #Mostrar prueba de serie aui
                                print("Prueba de serie")
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                            elif  Puntero_Interno4 == 3:
                                #Mostrar prueba de poker aui
                                print("Prueba de poker")
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                            elif Puntero_Interno4 == 4:
                                ReiniciarArreglos(returnTabla())
                                ReiniciarListas(returnDatos())
                                ReiniciarListas(returnRecurrrencias())
                                break
                    elif Puntero_Interno3 == 2:
                        ReiniciarArreglos(returnTabla())
                        ReiniciarListas(returnDatos())
                        ReiniciarListas(returnRecurrrencias())
                        break
            elif Puntero_Interno2 == 3:
                break


def menuPrincipal():
    while contador == True:
        print("############################ MENU ###################################")
        print("Bienvenido al menu de las pruebas de independencia y uniformidad")
        print("\n")
        print("1.Probar generadores")
        print("2.Pruebas de uniformidad e independencia")
        print("3.Salir")
        print("\n")

        Puntero_Menu = int(input("Eliga una opcion:"))
        while (Puntero_Menu > 4 or Puntero_Menu < 1):
            Puntero_Menu = int(input("Eliga una numero entero entre 1 y 4 no es tan dificil:"))
        if Puntero_Menu == 1:
            probar_generadores()
        elif Puntero_Menu == 2:
            menuUniformidad()
            #Prubas_Uniformidad_independencia()
        else:
            break
        print("##################### FIN DEL PROGRAMA ##############################")
