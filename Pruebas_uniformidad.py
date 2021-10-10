from decimal import *
import  generadores as ge
import math
ChiCalculadoTabla = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
KolmogorovCalculado =  [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
FOA = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
#"""TablaFrecuencia,datosGenerados""" parametros prueba x2
def PruebaChiCuadrado(modo,datosGenerados):
    #datosGenerados = int(input("Cuantos datos desea generar: "))
    if modo ==1 :
        ge.generadorlincong(datosGenerados)
    elif modo == 2:
        ge.generadorestmin(datosGenerados)
    else:
        ge.generadorPython(datosGenerados)
    TablaFrecuencia = ge.returnTabla()
    #datosGenerados = #1000
    Xcritico = 16.92#float(input("Ingrese el chi critico: "))
    ChiCalculado(TablaFrecuencia,datosGenerados)
    DibujarTabla(TablaFrecuencia,Xcritico,datosGenerados)
    if sum(ChiCalculadoTabla) <= Xcritico:
        print("")
        print("Segun la prueba de Chi cuadrado el generador es BUENO!!! en cuanto a uniformidad")
        print("ChiCalculado es: ",sum(ChiCalculadoTabla))
        print("Segun la prueba chiCuadrado: ChiCalculado <= chicritico")
        print(sum(ChiCalculadoTabla),"<=",Xcritico)
        print("")
    else:
        print("")
        print("Segun la prueba de Chi cuadrado el generador NO!!!!! es bueno en cuanto a uniformidad")
        print("ChiCalculado es: ",sum(ChiCalculadoTabla))
        print("Segun la prueba chiCuadrado: ChiCalculado <= chicritico")
        print(sum(ChiCalculadoTabla),">",Xcritico)
        print("")

def ChiCalculado(TablaFrecuencia,datosGenerados):
    getcontext()
    getcontext().prec = 2
    for i in range(10):
        cuadrado =(datosGenerados/10 - TablaFrecuencia[i])**2
        ChiCalculadoTabla[i] = cuadrado / (datosGenerados/10)


def DibujarTabla(TablaFrecuencia,xc,datosGenerados):
    getcontext()
    getcontext().prec = 1
    rango = 0
    print("  Rango  |   FE   |   FO     |  (FE - FO)^2 / FE | ")
    for i in range(10):
        print(rango,"-" ,rango +Decimal(0.1)," | ",TablaFrecuencia[i]," | ",datosGenerados/10,"      |",ChiCalculadoTabla[i])
        rango =Decimal( rango + Decimal(0.1))


def CalcKolmogorov(TablaFrecuencia,numerodatos):
    getcontext()
    getcontext().prec = 3
    Rango = Decimal(0.1)
    for i in range(10):
        KolmogorovCalculado[i] = abs (Rango - Decimal(Decimal(FOA[i])/numerodatos))
        Rango += Decimal(0.1)
#TablaFrecuencia,datosGenerados
def PruebaKolmogorov(modo,datosGenerados):
    #GradosLibertad = 999
    #datosGenerados = 1000
    if modo ==1:
        ge.generadorlincong(datosGenerados)
    elif modo == 2:
        ge.generadorestmin(datosGenerados)
    else:
        ge.generadorPython(datosGenerados)
    TablaFrecuencia = ge.returnTabla()
    Dmcritico = 1.36 / math.sqrt(datosGenerados)
    CalcularFOA(TablaFrecuencia)
    CalcKolmogorov(TablaFrecuencia,datosGenerados)
    DibujarKolmogorov(TablaFrecuencia,datosGenerados)

    if max(KolmogorovCalculado) <= Dmcritico:
        print("")
        print("Segun la prueba de Kolmogorov el generador es BUENO!!! en cuanto a uniformidad")
        print(max(KolmogorovCalculado)," <= ",Dmcritico)
        print("")
    else:
        print("")
        print("Segun la prueba de Kolmogorov el generador NO!!!!! es bueno en cuanto a uniformidad")
        print(min(KolmogorovCalculado)," > ",Dmcritico)
        print("")
def CalcularFOA(TablaFrecuencia):

    for i in range(10):
        if i == 0:
            FOA[i] = TablaFrecuencia[i]
        else:
            FOA [i] = TablaFrecuencia[i]+FOA[i-1]
def DibujarKolmogorov(TablaFrecuencia,datosGenerados):
    getcontext()
    getcontext().prec = 1
    rango = 0
    print("  Rango  |   FO   |   FOA     |    POA  |  PEA  | |PEA  - POA | ")
    for i in range(10):
        print(rango,"-" ,rango +Decimal(0.1)," | ",TablaFrecuencia[i]," | ", FOA[i],"  |   ",FOA[i]/datosGenerados,"  |  ",rango+Decimal(0.1),"     |  ",KolmogorovCalculado[i])
        rango =Decimal( rango + Decimal(0.1))
