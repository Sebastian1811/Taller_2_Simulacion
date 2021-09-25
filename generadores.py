import Pruebas_uniformidad

Tabla = [0,0,0,0,0,0,0,0,0,0]

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


def generadorlincong():
    a = int(input("a es: "))
    c = int(input("c es: "))
    m = int(input("m es: "))
    Xo = int(input("Xo es: "))
    n = int(input("Cantidad de número que desea generar: "))
    print()
    print(Xo)
    res = (a * Xo + c) % m
    EvaluarRecurrencia(res,m)
    print(res)
    for i in range(n-1):
        res = (a * res + c) % m
        EvaluarRecurrencia(res,m)
        print(res)
    ChiCalculado(Tabla)
    PruebaChiCuadrado(sum(ChiCalculadoTabla))

def generadorestmin():
    a = int(input("a es: "))
    m = int(input("m es: "))
    Xo = int(input("Xo es: "))
    n = int(input("Cantidad de número que desea generar: "))
    print()
    print(Xo)
    res = (a * Xo) % m
    print(res)
    for i in range(n-1):
        res = (a * res) % m
        print(res)

generadorlincong()

#generadorestmin()

# a = 28
# c = 14
# m = 100
# Xo = 27

""" Linear Congruente
27 70 74 86 22 30 54 26 42 90
34 66 62 50 14 6  82 10 94 2
70 74 86 22 30 54 26 42 90 34
66 62 50 14 6  82 10 94 46 2
*70 74 86 22 30 54 26 42 90 34

* = donde se vuelve a generar el patrón
"""

""" Linear Congruente
27 56 68 4  12 36 8  24 72 16
48 44 32 96 88 64 92 76 28 84
52 *56 68 4  12 36 8  24 72 16
48 44 32 96 88 64 92 76 28 84
52 56 68 4  12 36 8  24 72 16

* = donde se vuelve a generar el patrón
"""
