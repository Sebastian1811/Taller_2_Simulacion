import Pruebas_uniformidad as Prueba
Tabla = [0,0,0,0,0,0,0,0,0,0]
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
def ReiniciarTabla():
    for i in range(10):
        Tabla[i] = 0

def generadorlincong():
    a = int(input("a es: "))
    c = int(input("c es: "))
    m = int(input("m es: "))
    Xo = int(input("Xo es: "))
    global n
    n = 1000#int(input(" cuantos datos desea generar: "))
    print()
    #print(Xo)
    res = (a * Xo + c) % m
    EvaluarRecurrencia(res,m)
    #print(res)
    for i in range(n-1):
        res = (a * res + c) % m
        EvaluarRecurrencia(res,m)
        #print(res)

    #Prueba.PruebaChiCuadrado(Tabla,n)

    #Prueba.PruebaKolmogorov(Tabla,n)

def generadorestmin():
    a = int(input("a es: "))
    m = int(input("m es: "))
    Xo = int(input("Xo es: "))
    global n
    n = 1000#int(input(" cuantos datos desea generar: "))
    print()
    print(Xo)
    res = (a * Xo) % m
    EvaluarRecurrencia(res,m)
    print(res)
    for i in range(n-1):
        res = (a * res) % m
        EvaluarRecurrencia(res,m)
    #Prueba.ChiCalculado(Tabla)
    #Prueba.PruebaChiCuadrado(Tabla)
        #print(res)
