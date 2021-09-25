from decimal import *
ChiCalculadoTabla = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]


def PruebaChiCuadrado():
    Xcritico = 16.92#float(input("Ingrese el chi critico: "))
    if sum(ChiCalculadoTabla) <= Xcritico:
        DibujarTabla()
        print("Segun la prueba de Chi cuadrado el generador es bueno en cuanto a uniformidad")
    else:
        print("Segun la prueba de Chi cuadrado el generador NO!!!!! es bueno en cuanto a uniformidad")

def ChiCalculado(TablaFrecuencia):
    for i in range(10):
        ChiCalculadoTabla[i] = (100 - TablaFrecuencia[i])* (100 - TablaFrecuencia[i])/ 100

def DibujarTabla():
    getcontext()
    getcontext().prec = 1
    rango = 0
    print("  Rango  | FE | FO | (FE - FO)^2 / FE | ")
    for i in range(10):
        print(rango,"-" ,rango +Decimal(0.1))
        rango =Decimal( rango + Decimal(0.1))
