import Pruebas_uniformidad as Prueba
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
    a = 106#int(input("a es: "))
    c = 1283#int(input("c es: "))
    m = 6075#int(input("m es: "))
    Xo = 5#int(input("Xo es: "))
    n =1000
    print()
    print(Xo)
    res = (a * Xo + c) % m
    EvaluarRecurrencia(res,m)
    print(res)
    for i in range(n-1):
        res = (a * res + c) % m
        EvaluarRecurrencia(res,m)
        #print(res)
    Prueba.ChiCalculado(Tabla)
    Prueba.PruebaChiCuadrado(Tabla)

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


#generadorlincong()

#generadorestmin()
