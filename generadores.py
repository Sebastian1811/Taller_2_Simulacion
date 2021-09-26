import Pruebas_uniformidad as Prueba
import random
from decimal import *
Tabla = [0,0,0,0,0,0,0,0,0,0]
datosGenerados = list()
recurrencias = list()
n = 0
def EvaluarRecurrencia(Xn,m):
    Rn = Xn/m
    if Rn < 0.1 and Rn >= 0:
        Tabla[0] += 1
    elif Rn < 0.2 and Rn >= 0.1:
        Tabla[1] += 1
    elif Rn < 0.3 and Rn >= 0.2:
        Tabla[2] += 1
    elif Rn < 0.4 and Rn >= 0.3:
        Tabla[3] += 1
    elif Rn < 0.5 and Rn >= 0.4:
        Tabla[4] += 1
    elif Rn < 0.6 and Rn >= 0.5:
        Tabla[5] += 1
    elif Rn < 0.7 and Rn >= 0.6:
        Tabla[6] += 1
    elif Rn < 0.8 and Rn >= 0.7:
        Tabla[7] += 1
    elif Rn < 0.9 and Rn >= 0.8:
        Tabla[8] += 1
    else:
        Tabla[9] += 1
def returnTabla():
    return Tabla
def returnN():
    return n
def ReiniciarArreglos(Arreglo):
    for i in range(len(Arreglo)):
        Arreglo[i] = 0
def ReiniciarListas(lista):
    while lista != []:
        lista.pop()

def generadorlincong(Datosrequeridos):
    a = int(input("a es: "))
    c = int(input("c es: "))
    m = int(input("m es: "))
    Xo = int(input("Xo es: "))
    global n
    n = Datosrequeridos #int(input(" cuantos datos desea generar: "))
    print()
    #print(Xo)
    datosGenerados.append(Xo)
    recurrencias.append(round(Xo/m,3))
    res = (a * Xo + c) % m
    EvaluarRecurrencia(res,m)
    #print(res)
    for i in range(n-1):
        res = (a * res + c) % m
        datosGenerados.append(res)
        recurrencias.append(round(res/m,3))
        EvaluarRecurrencia(res,m)
        #print(res)

def generadorestmin(Datosrequeridos):
    a = int(input("a es: "))
    m = int(input("m es: "))
    Xo = int(input("Xo es: "))
    global n
    n = Datosrequeridos#int(input(" cuantos datos desea generar: "))
    print()
    #print(Xo)
    res = (a * Xo) % m
    datosGenerados.append(Xo)
    recurrencias.append(round(Xo/m,3))
    EvaluarRecurrencia(res,m)
    print(res)
    for i in range(n-1):
        res = (a * res) % m
        datosGenerados.append(res)
        recurrencias.append(round(res/m,3))
        EvaluarRecurrencia(res,m)
def generadorPython(Datosrequeridos):
    global n
    n = Datosrequeridos
    for i in range(Datosrequeridos):
        res = random.randint(1,500)
        datosGenerados.append(res)
        recurrencias.append(res/500)
        EvaluarRecurrencia(res,500)

def HallarPeriodo():
    Periodo = datosGenerados.index(datosGenerados[0],1) + 1
    return Periodo
def VerDatosGenerados(datos):
    for i in range(len(datos)):
        print(datos[i])

generadorlincong(10)
VerDatosGenerados(recurrencias)
