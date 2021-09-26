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


def Prubas_Uniformidad_independencia():
    while True:
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
            print("######################## Bienvenido al menu del generador lineal congruente ####################################")
            print("1.Prueba de x2")
            print("2.Prueba kolmogorov")
            print("3.Volver")
            print("############################################################")
            Puntero_Interno2 = int(input("Eliga una opcion:"))
            while (Puntero_Interno2 > 3 or Puntero_Interno2 < 1):
                Puntero_Interno2 = int(input("Eliga una opcion:"))
            while 1:
                if Puntero_Interno2 == 1:
                    #Prueba del chi cuadrado aqui
                    print("\n")
                    print("/////////PRUEBA DE chi cuadrado////////////////")
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
                                break
                            elif Puntero_Interno4 == 2:
                                #Mostrar prueba de serie aqui
                                print("Prueba de serie")
                                break
                            elif  Puntero_Interno4 == 3:
                                #Mostrar prueba de poker aqui
                                print("Prueba de poker")
                                break
                            elif Puntero_Interno4 == 4:
                                break
                    elif Puntero_Interno3 == 2:
                        break
                elif Puntero_Interno2 == 2:
                    #Prueba de kolmogorov aqui
                    print("\n")
                    print("/////////PRUEBA DE KOLMOGOROV////////////////")
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
                                break
                            elif Puntero_Interno4 == 2:
                                #Mostrar prueba de serie aqui
                                print("Prueba de serie")
                                break
                            elif  Puntero_Interno4 == 3:
                                #Mostrar prueba de poker aqui
                                print("Prueba de poker")
                                break
                            elif Puntero_Interno4 == 4:
                                break
                    elif Puntero_Interno3 == 2:
                        break     
                elif Puntero_Interno2 == 3: 
                    break
        elif Puntero_Interno == 2:
            print("######################## Bienvenido al menu del generador Estandar minimo ####################################")
            print("1.Prueba de x2")
            print("2.Prueba kolmogorov")
            print("3.Volver")
            print("############################################################")
            Puntero_Interno2 = int(input("Eliga una opcion:"))
            while (Puntero_Interno2 > 3 or Puntero_Interno2 < 1):
                Puntero_Interno2 = int(input("Eliga una opcion:"))
            while 1:
                if Puntero_Interno2 == 1:
                    #Prueba del chi cuadrado aqui
                    print("\n")
                    print("/////////PRUEBA DE chi cuadrado////////////////")
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
                                break
                            elif Puntero_Interno4 == 2:
                                #Mostrar prueba de serie aqui
                                print("Prueba de serie")
                                break
                            elif  Puntero_Interno4 == 3:
                                #Mostrar prueba de poker aqui
                                print("Prueba de poker")
                                break
                            elif Puntero_Interno4 == 4:
                                break
                    elif Puntero_Interno3 == 2:
                        break
                elif Puntero_Interno2 == 2:
                    #Prueba de kolmogorov aqui
                    print("\n")
                    print("/////////PRUEBA DE KOLMOGOROV////////////////")
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
                                break
                            elif Puntero_Interno4 == 2:
                                #Mostrar prueba de serie aui
                                print("Prueba de serie")
                                break
                            elif  Puntero_Interno4 == 3:
                                #Mostrar prueba de poker aui
                                print("Prueba de poker")
                                break
                            elif Puntero_Interno4 == 4:
                                break
                    elif Puntero_Interno3 == 2:
                        break     
                elif Puntero_Interno2 == 3: 
                    break
        elif  Puntero_Interno == 3:
            break        
            
        



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
        Prubas_Uniformidad_independencia()
    else:
        break
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
