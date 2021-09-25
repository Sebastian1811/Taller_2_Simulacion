from decimal import *
import math
ChiCalculadoTabla = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
KolmogorovCalculado =  [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
FOA = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

def PruebaChiCuadrado(TablaFrecuencia,datosGenerados):
    Xcritico = 16.92#float(input("Ingrese el chi critico: "))
    ChiCalculado(TablaFrecuencia,datosGenerados)
    DibujarTabla(TablaFrecuencia,Xcritico,datosGenerados)
    if sum(ChiCalculadoTabla) <= Xcritico:
        print("Segun la prueba de Chi cuadrado el generador es BUENO!!! en cuanto a uniformidad")
        print("ChiCalculado es: ",sum(ChiCalculadoTabla))
        print("Segun la prueba chiCuadrado: ChiCalculado <= chicritico")
        print(sum(ChiCalculadoTabla),"<=",xc)
    else:
        print("Segun la prueba de Chi cuadrado el generador NO!!!!! es bueno en cuanto a uniformidad")
        print("ChiCalculado es: ",sum(ChiCalculadoTabla))
        print("Segun la prueba chiCuadrado: ChiCalculado <= chicritico")
        print(sum(ChiCalculadoTabla),">",xc)
        
def ChiCalculado(TablaFrecuencia,datosGenerados):
    for i in range(10):
        ChiCalculadoTabla[i] = (datosGenerados - TablaFrecuencia[i])* (datosGenerados - TablaFrecuencia[i])/ datosGenerados


def DibujarTabla(TablaFrecuencia,xc,datosGenerados):
    getcontext()
    getcontext().prec = 1
    rango = 0
    print("  Rango  |   FE   |   FO     |  (FE - FO)^2 / FE | ")
    for i in range(10):
        print(rango,"-" ,rango +Decimal(0.1)," | ",TablaFrecuencia[i]," | ",datosGenerados,"      |",ChiCalculadoTabla[i])
        rango =Decimal( rango + Decimal(0.1))


def CalcKolmogorov(TablaFrecuencia,numerodatos):
    getcontext()
    getcontext().prec = 3
    Rango = Decimal(0.1)
    for i in range(10):
        KolmogorovCalculado[i] = abs (Rango - Decimal(Decimal(FOA[i])/numerodatos))
        Rango += Decimal(0.1)

def PruebaKolmogorov(TablaFrecuencia,datosGenerados):
    GradosLibertad = 999
    Dmcritico = 1.36 / math.sqrt(datosGenerados)
    CalcularFOA(TablaFrecuencia)
    CalcKolmogorov(TablaFrecuencia,datosGenerados)
    DibujarKolmogorov(TablaFrecuencia,datosGenerados)

    if max(KolmogorovCalculado) <= Dmcritico:

        print("Segun la prueba de Kolmogorov el generador es BUENO!!! en cuanto a uniformidad")
        print(max(KolmogorovCalculado)," <= ",Dmcritico)
    else:
        print("Segun la prueba de Kolmogorov el generador NO!!!!! es bueno en cuanto a uniformidad")
        print(min(KolmogorovCalculado)," > ",Dmcritico)

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
