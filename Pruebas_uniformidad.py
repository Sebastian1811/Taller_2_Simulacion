ChiCalculadoTabla = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]


def PruebaChiCuadrado(Xcalculado):
    Xcritico = float(input("Ingrese el chi critico: "))
    if Xcalculado <= Xcritico:
        print("Segun la prueba de Chi cuadrado el generador es bueno en cuanto a uniformidad")
    else:
        print("Segun la prueba de Chi cuadrado el generador NO!!!!! es bueno en cuanto a uniformidad")

def ChiCalculado(TablaFrecuencia):
    for i in range(10):
        ChiCalculadoTabla[i] = (100 - Tabla[i])* (100 - Tabla[i])/ 100
