import math
corridas = list()
TablaSeries = [
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]
]
TablaSeriesCalc = [
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
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
        print("No hay evidencia para rechazar la hipotesis de independencia")
        print(Zo,"<",Zobs,"<",Z)
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
    return listaPares

def UbicarPares(ParesRecurrencias):

    for i in range(len(ParesRecurrencias)):
        for j in range(1):
            if ParesRecurrencias[i][j] < 0.2 and ParesRecurrencias[i][j] >= 0:
                if ParesRecurrencias[i][j+1] < 0.2  and ParesRecurrencias[i][j+1]>= 0:
                    TablaSeries[0][0] += 1
                elif ParesRecurrencias[i][j+1] < 0.4  and ParesRecurrencias[i][j+1]>= 0.2:
                    TablaSeries[0][1] += 1
                elif ParesRecurrencias[i][j+1] < 0.6  and ParesRecurrencias[i][j+1]>= 0.4:
                    TablaSeries[0][2] += 1
                elif ParesRecurrencias[i][j+1] < 0.8  and ParesRecurrencias[i][j+1]>= 0.6:
                    TablaSeries[0][3] += 1
                elif ParesRecurrencias[i][j+1] < 1  and ParesRecurrencias[i][j+1]>= 0.8:
                    TablaSeries[0][4] += 1

            elif ParesRecurrencias[i][j] < 0.4 and ParesRecurrencias[i][j] >= 0.2:
                if ParesRecurrencias[i][j+1] < 0.2  and ParesRecurrencias[i][j+1]>= 0:
                    TablaSeries[1][0] += 1
                elif ParesRecurrencias[i][j+1] < 0.4  and ParesRecurrencias[i][j+1]>= 0.2:
                    TablaSeries[1][1] += 1
                elif ParesRecurrencias[i][j+1] < 0.6  and ParesRecurrencias[i][j+1]>= 0.4:
                    TablaSeries[1][2] += 1
                elif ParesRecurrencias[i][j+1] < 0.8  and ParesRecurrencias[i][j+1]>= 0.6:
                    TablaSeries[1][3] += 1
                elif ParesRecurrencias[i][j+1] < 1 and ParesRecurrencias[i][j+1]>= 0.8:
                    TablaSeries[1][4] += 1

            elif ParesRecurrencias[i][j] < 0.6 and ParesRecurrencias[i][j] >= 0.4:
                if ParesRecurrencias[i][j+1] < 0.2  and ParesRecurrencias[i][j+1]>= 0:
                    TablaSeries[2][0] += 1
                elif ParesRecurrencias[i][j+1] < 0.4  and ParesRecurrencias[i][j+1]>= 0.2:
                    TablaSeries[2][1] += 1
                elif ParesRecurrencias[i][j+1] < 0.6  and ParesRecurrencias[i][j+1]>= 0.4:
                    TablaSeries[2][2] += 1
                elif ParesRecurrencias[i][j+1] < 0.8  and ParesRecurrencias[i][j+1]>= 0.6:
                    TablaSeries[2][3] += 1
                elif ParesRecurrencias[i][j+1] < 1 and ParesRecurrencias[i][j+1]>= 0.8:
                    TablaSeries[2][4] += 1

            elif ParesRecurrencias[i][j] < 0.8 and ParesRecurrencias[i][j] >= 0.6:
                if ParesRecurrencias[i][j+1] < 0.2  and ParesRecurrencias[i][j+1]>= 0:
                    TablaSeries[3][0] += 1
                elif ParesRecurrencias[i][j+1] < 0.4  and ParesRecurrencias[i][j+1]>= 0.2:
                    TablaSeries[3][1] += 1
                elif ParesRecurrencias[i][j+1] < 0.6  and ParesRecurrencias[i][j+1]>= 0.4:
                    TablaSeries[3][2] += 1
                elif ParesRecurrencias[i][j+1] < 0.8  and ParesRecurrencias[i][j+1]>= 0.6:
                    TablaSeries[3][3] += 1
                elif ParesRecurrencias[i][j+1] < 1  and ParesRecurrencias[i][j+1]>= 0.8:
                    TablaSeries[3][4] += 1

            elif ParesRecurrencias[i][j] < 1 and ParesRecurrencias[i][j] >= 0.8:
                if ParesRecurrencias[i][j+1] < 0.2  and ParesRecurrencias[i][j+1]>= 0:
                    TablaSeries[4][0] += 1
                elif ParesRecurrencias[i][j+1] < 0.4  and ParesRecurrencias[i][j+1]>= 0.2:
                    TablaSeries[4][1] += 1
                elif ParesRecurrencias[i][j+1] < 0.6  and ParesRecurrencias[i][j+1]>= 0.4:
                    TablaSeries[4][2] += 1
                elif ParesRecurrencias[i][j+1] < 0.8  and ParesRecurrencias[i][j+1]>= 0.6:
                    TablaSeries[4][3] += 1
                elif ParesRecurrencias[i][j+1] < 1  and ParesRecurrencias[i][j+1]>= 0.8:
                    TablaSeries[4][4] += 1
def CalcularChi(TablaFrecuencia,datosGenerados):
    FE = (datosGenerados/2) / 25
    for i in range(len(TablaFrecuencia)):
        for j in range(len(TablaFrecuencia)):
            numerador = (FE - TablaSeries[i][j])**2
            TablaSeriesCalc[i][j] = numerador / FE

def pruebaSeries(recurrencias):
    Xcritico = 36.42
    Xcalc = 0
    UbicarPares(MapearPares(recurrencias))
    CalcularChi(TablaSeries,1000)
    for i in range(len(TablaSeriesCalc)):
        for j in range(len(TablaSeriesCalc)):
            Xcalc += TablaSeriesCalc[i][j]
    if Xcalc <= Xcritico:
        print( "Como Xcalc"+ " <= "+ "X2crit SE ACEPTA!!! la hipotesis de que los datos tienen distribucion uniforme bidimensional")
        print("")
        print(Xcalc," <= ",Xcritico)
        print("")
    else:
        print( "Como Xcalc "+ ">"+ " X2crit NO SE ACEPTA!!! la hipotesis de que los datos tienen distribucion uniforme bidimensional")
        print("")
        print(Xcalc," > ",Xcritico)
        print("")

def calcularPoker(recurrencias):
    casos = [0, 0, 0]
    datos = list()
    digitos = list()
    datos = recurrencias
    for i in range(len(datos)):
        numero = str(datos[i])
        if len(numero) == 3: # Este if y el elif que sigue es para que todos los numeros tengan la misma cantidad de digitos
            numero = numero + '0' + '0'
        elif len(numero) == 4:
            numero = numero + '0'
        numeroDec = numero.replace('0.','') # Quita el 0. de los numeros porque no sirven para la prueba
        digitos = [int(i) for i in str(numeroDec)] # Separa el numero en digitos para hacer la comprobación
        # Se colocan los numeros en sus respectivos casos
        if digitos[0] == digitos[1]:
            casos[1]
        if digitos[0] == digitos[1] and digitos[1] == digitos[2]:
            casos[2] += 1
        elif digitos[0] != digitos[1] and digitos[0] != digitos[2] and digitos[1] != digitos[2]:
            casos[0] += 1
        else: casos[1] += 1
    return casos

def pruebaPoker(recurrencias):
    FO = calcularPoker(recurrencias)
    FE = [720, 270, 10]
    Xcalc = 0
    Xcritico = 5.99
    for i in range(len(FO)):
        Xcalc += round(((FO[i]-FE[i])**2)/FE[i], 4)
    if Xcalc <= Xcritico:
        print("Como Xcalc" + " <= " + "Xcrit SE ACEPTA!!! la hipotesis de que los datos tienen una independencia")
        print("")
        print(round(Xcalc,3), " <= ",round(Xcritico,3))
        print("")
    else:
        print("Como Xcalc" + " <= " + "Xcrit NO SE ACEPTA!!! la hipotesis de que los datos tienen una independencia")
        print("")
        print(round(Xcalc,3), " > ",round(Xcritico,3))
        print("")


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
