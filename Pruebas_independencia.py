
def PruebaCorridas(recurrencias ):
    Varianza = (2000-1)/3
    Media = ((16*1000)-29)/90
    Z = 1.96
    Zo = -1.96
    Corridas = 0
    ValCorrida = 0
    pos = 0
    neg = 0
    for i in range(len(recurrencias)-1):
        if i == 0:
            if recurrencias[i] > recurrencias[i+1]:
                pos = 1
            else:
                neg = 1
            ValCorrida = recurrencias[i+1]
        elif pos and recurrencias[i] < recurrencias[i+1]:
            ValCorrida = recurrencias[i+1]
        elif neg and recurrencias[i] > recurrencias[i+1] :
            ValCorrida = recurrencias[i+1]
        elif pos and recurrencias[i] > recurrencias[i+1] :
            ValCorrida = recurrencias[i+1]
            pos = 0
            neg = 1
            Corridas+=1
        elif neg and recurrencias[i] < recurrencias[i+1]:
            ValCorrida = recurrencias[i+1]
            pos = 1
            neg = 0
            Corridas+=1
    print(Corridas)

"""PruebaCorridas([0.08, 0.09, 0.23, 0.29, 0.42, 0.55, 0.58, 0.72, 0.89, 0.91,
0.11, 0.16, 0.18, 0.31, 0.41, 0.53, 0.71, 0.73, 0.74, 0.84,
0.01, 0.09, 0.30, 0.32, 0.45, 0.47, 0.69, 0.74, 0.91, 0.95,
0.12, 0.13, 0.29, 0.36, 0.38, 0.54, 0.68, 0.86, 0.88, 0.91])"""
