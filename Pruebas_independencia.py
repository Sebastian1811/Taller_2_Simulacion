import math
corridas = list()
TablaSeries = [
[0,0,0,0,0]
[0,0,0,0,0]
[0,0,0,0,0]
[0,0,0,0,0]
[0,0,0,0,0]
]
def ContarCorridas(recurrencias ):
    Corridas = 0
    ValCorrida = 0
    pos = 0
    neg = 0
    for i in range(len(recurrencias)-1):
        if i == 0:
            corridas.append("*")
            if recurrencias[i] > recurrencias[i+1]:
                pos = 1
                corridas.append("-")
            elif recurrencias[i] < recurrencias[i+1]:
                neg = 1
                corridas.append("+")
            ValCorrida = recurrencias[i+1]
        elif pos and recurrencias[i] < recurrencias[i+1]:
            ValCorrida = recurrencias[i+1]
            corridas.append("+")
        elif neg and recurrencias[i] > recurrencias[i+1] :
            ValCorrida = recurrencias[i+1]
            corridas.append("-")
        elif pos and recurrencias[i] > recurrencias[i+1] :
            ValCorrida = recurrencias[i+1]
            pos = 0
            neg = 1
            Corridas+=1
            corridas.append("-")
        elif neg and recurrencias[i] < recurrencias[i+1]:
            ValCorrida = recurrencias[i+1]
            pos = 1
            neg = 0
            Corridas+=1
            corridas.append("+")
    return Corridas

def PruebaCorridas(recurrencias,N):
    Corridas = ContarCorridas(recurrencias)
    Varianza = ((2*N)-1)/3
    Media = ((16*N)-29)/90
    Z = 1.96
    Zo = -1.96
    hipotesis = 0
    numerador = Corridas - Varianza
    denominador = math.sqrt(Media)
    Zobs =  round(numerador / denominador,3)
    mostrarCorridas(recurrencias,"Secuencia")
    mostrarCorridas(corridas,"Comportamiento de crecimiento-decrecimiento")
    if Zobs < Z and Zobs > Zo:
        hipotesis = 1
    if hipotesis:
        print("Hay en total: ",Corridas," corridas")
        print("No hay evidencia para rechar la hipotesis de independencia")
        print(Zo,"<",Zobs,">",Z)
    else:
        print("Hay en total: ",Corridas," corridas")
        print("Se rechaza la hipotesis de independencia")
        print(Zobs, " Esta fuera del intervalo ", "[",Zo," , ",Z," ]")

def mostrarCorridas(corridas,titulo):
    contador = 0
    print("")
    print("////////////////// "+titulo+" //////////////////")
    print("")
    for i in range(int(len(corridas)/10)):
        for i in range(10):
            if contador < len(corridas):
                print(corridas[contador]," ",end=" ")
                contador+=1
        print("")
    print("")
    print("////////////////////////////////////////////////////")


def MapearPares(recurrencias):
    listaPares = list()
    count = 0
    for i in range(len(recurrencias)-1):
        if count < (len(recurrencias)-1):
            listaPares.append([recurrencias[count],recurrencias[count+1]])
            count+=2
            #print(count)
    return listaPares
#def pruebaSeries(recurrencias):


# /////////// PRUEBAS ////////////
array1 = [0.41, 0.68, 0.89, 0.94, 0.74, 0.91, 0.55, 0.62, 0.36, 0.27,
0.19, 0.72, 0.75 ,0.08, 0.54, 0.02, 0.01, 0.36, 0.16, 0.28,
0.18, 0.01, 0.95, 0.69, 0.18, 0.47, 0.23, 0.32, 0.82, 0.53,
0.31, 0.42, 0.73, 0.04, 0.83, 0.45, 0.13, 0.57, 0.63, 0.29
]
array2 = [0.08, 0.09, 0.23, 0.29, 0.42, 0.55, 0.58, 0.72, 0.89, 0.91,
0.11, 0.16, 0.18, 0.31, 0.41, 0.53, 0.71, 0.73, 0.74, 0.84,
0.01, 0.09, 0.30, 0.32, 0.45, 0.47, 0.69, 0.74, 0.91, 0.95,
0.12, 0.13, 0.29, 0.36, 0.38, 0.54, 0.68, 0.86, 0.88, 0.91]
#PruebaCorridas(array1,40)
#PruebaCorridas(array1,40)"""

"""print(MapearPares(array1))
print(len(MapearPares(array1)))
"""
