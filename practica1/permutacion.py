import argparse
from curses.ascii import islower
from fileinput import close
import os
import numpy as np
import string
from gmpy2 import mpz
from euclides_extendido import inverso_multiplicativo



#EJECUCION:
#   python afin.py --mode C --m 26 --a 15 --b hola --i input.txt --o output.txt
print("--------------\nCIFRADO PERMUTACION DE CRIPTOSISTEMAS\n--------------\npython permutacion.py --help  Para obtener ayuda\n")

abecedario = list(string.ascii_lowercase)
input = "input.txt"
output = "output.txt"
size = 26

parser = argparse.ArgumentParser(description='Parse the func action')
parser.add_argument('--mode', dest='mode', nargs='+', default=False,
                        help='indica el modo de ejecucion --mode D para descifrar y --mode C para cifrar')
parser.add_argument('--k1', dest='k1', nargs='+', default=False,
                        help='indica la clave k1')
parser.add_argument('--k2', dest='k2', nargs='+', default=False,
                        help='indica la clave k2')
parser.add_argument('--i', dest='i', nargs='+', default=False,
                        help='indica el nombre del fichero input')
parser.add_argument('--o', dest='o', nargs='+', default=False,
                        help='indica el nombre del fichero output')
args = parser.parse_args()

if args.mode:
    if args.mode[0] == 'C':
        print("Modo cifrado")
        mode = 0 #Modo cifrar
    else:
        print("Modo descifrado")
        mode = 1 #Modo descifrar

if args.k1:
    k1 = []
    for arg in args.k1:
        k1.append(int(arg))

if args.k2:
    k2 = []
    for arg in args.k2:
        k2.append(int(arg))

if args.i:
    input = args.i[0]

if args.o:
    output = args.o[0]

if not args.k1 or not args.k2:
    print("Error en formato de entrada. Ejemplo de formato correcto:\npython permutacion.py --k1 5 --k2 26 --i input.txt --o output.txt")
    exit(0)


entrada = open(os.getcwd()+"/ficheros/" + input)
caracter = " "

if mode == 0:
    listalet = []
    listaAux = []
    caractCif = []
    matrix = []
    matrixCar = []
    lon = 0
    #Leo caracter a caracter
    while caracter != "":
        caracter = entrada.readline(1)
        #En caso de que sea letra
        if caracter == '\n':
            if len(listaAux) != lon and lon != 0 and len(listaAux) != 0:
                #add padding
                numpad = lon - len(listaAux)
                for i in range(0,numpad):
                    listaAux.append(25)
                    listalet.append('z')
            if len(listaAux) != 0:
                matrix.append(listaAux)
            if lon == 0:
                lon = len(listaAux)
            matrixCar.append(listalet)
            listalet = []
            listaAux = []
            
        elif caracter != " " and caracter != '' and caracter != '.' and caracter != ',':
            caracter = caracter.lower()
            if caracter.islower() == True:
                #anyado a una lista el valor numerico
                listalet.append(caracter)
                listaAux.append(abecedario.index(caracter))
    entrada.close()
    print("\nTexto Claro:")
    for fila in matrix:
        print("".join(str(fila)))

    matrixSalida = []
    index = 0
    #Aplicar K1
    for index in range(0,len(matrix)):
        fila = matrix[k1[index]]
        matrixSalida.append(fila)


    matrixAux = matrixSalida
    matrixSalida = []
    matrixCarSalida = []
    #Aplico K2
    indexFila = 0
    for fila in matrixAux:
        indexcol = 0
        matrixSalida.append([])
        matrixCarSalida.append([])
        for col in fila:
            ele = matrixAux[indexFila][int(k2[indexcol])]
            matrixSalida[indexFila].append(ele)
            matrixCarSalida[indexFila].append(abecedario[ele])
            indexcol = indexcol + 1 
        indexFila = indexFila +1

    print("--------\nTexto Cifrado: ")
    for fila in matrixCarSalida:
        print("".join(fila))

else:
    listalet = []
    listaAux = []
    caractCif = []
    matrix = []
    lon = 0
    #Leo caracter a caracter
    while caracter != "":
        caracter = entrada.readline(1)
        #En caso de que sea letra
        if caracter == '\n':
            if len(listaAux) != lon and lon != 0 and len(listaAux) != 0:
                #add padding
                numpad = lon - len(listaAux)
                for i in range(0,numpad):
                    listaAux.append(25)
            if len(listaAux) != 0:
                matrix.append(listaAux)
            if lon == 0:
                lon = len(listaAux)
            caractCif.append(listalet)
            listaAux = []
            listalet = []
            
        elif caracter != " " and caracter != '' and caracter != '.' and caracter != ',':
            caracter = caracter.lower()
            if caracter.islower() == True:
                #anyado a una lista el valor numerico
                listalet.append(caracter)
                listaAux.append(abecedario.index(caracter))
    entrada.close()
    print("\nTexto Cifrado:")
    for fila in caractCif:
        print("".join(fila))

    matrixSalida = []
    index = 0
    matrixAux = matrix    
    #Aplico K2
    indexFila = 0
    for fila in matrixAux:
        indexcol = 0
        matrixSalida.append([])
        for col in fila:
            indice = k2.index(indexcol)
            ele = matrixAux[indexFila][int(indice)]
            matrixSalida[indexFila].append(abecedario[ele])
            indexcol = indexcol + 1 
        indexFila = indexFila +1

    matrixAux = matrixSalida
    matrixSalida = []
    #Aplicar K1
    for index in range(0,len(matrix)):
        i = k1.index(index)
        fila = matrixAux[i]
        matrixSalida.append(fila)

    #Elimino padding
    while 'z' in matrixSalida[len(matrixSalida)-1]:
        matrixSalida[len(matrixSalida)-1].remove('z')

    
    print("--------\nTexto Claro: ")
    for fila in matrixSalida:
        print("".join(fila))