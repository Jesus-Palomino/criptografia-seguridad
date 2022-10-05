import argparse
from ctypes import sizeof
from fileinput import close
import os
import string
from gmpy2 import mpz
from euclides_extendido import inverso_multiplicativo
from mcd import mcd1
import pandas as pd


#EJECUCION:
#   python afin.py --mode C --m 26 --a 15 --b hola --i input.txt --o output.txt
print("--------------\nCRIPTOANALISIS VIGENERE\n--------------\npython cAnalisisVigenere.py --help  Para obtener ayuda\n")

abecedario = list(string.ascii_lowercase)
input = "texto_cifrado.txt"
output = "output.txt"
size = 26

parser = argparse.ArgumentParser(description='Parse the func action')
parser.add_argument('--mode', dest='mode', nargs='+', default=False,
                        help='indica el modo de ejecucion --mode K para Kasiski y --mode IC para Indice de Coincidencia')
parser.add_argument('--n', dest='n', nargs='+', default=False,
                        help='indica el numero de caracteres maximo')
parser.add_argument('--i', dest='i', nargs='+', default=False,
                        help='indica el nombre del fichero input')
parser.add_argument('--o', dest='o', nargs='+', default=False,
                        help='indica el nombre del fichero output')
args = parser.parse_args()

if args.mode:
    if args.mode[0] == 'K':
        print("Se ha elegido kasiski")
        mode = 0 #Modo Kasiski
    else:
        print("Se ha elegido Índice de Coincidencia")
        mode = 1 #Modo IC
if args.n:
    n = args.n[0]

if args.i:
    input = args.i[0]

if args.o:
    output = args.o[0]

entrada = open(os.getcwd()+"/ficheros/" + input)
caracter = " "
cadena = entrada.read()

#Modo kasiski
if mode == 0:
    
    listaMCD = []

    for i in range(2,int(n)):
        print("Probando con cadenas de " + str(i) + " Caractres")
        entradaAux = cadena
        distancias = []
        buscador = entradaAux[0:i]
        entradaAux = cadena[i:]
        contador = entradaAux.count(buscador)
        contadorAjuste = 0

        while contador != 0:
            distancia = 0
            contadorAjuste = contadorAjuste + 1
            contador = entradaAux.count(buscador)
            distancia_index = entradaAux.find(buscador)
            corte2 = distancia_index + i - contadorAjuste
            entradaAux = entradaAux[corte2:]
            if len(distancias) > 0:
                distancia_index = distancia_index + ult_dist
            ult_dist = distancia_index
            if contador != 0:
                distancias.append(distancia_index)
            

        for d in distancias:
            print("Distancia de la ocurrencia: " + str(d))
        print("----------")
        md = mcd1(distancias)
        if md != 1 and md != 0:
            listaMCD.append(md)
    print("el tamanio de clave posiblemente sea: " + str(listaMCD))


else:
    listaMedias = []
    for i in range(2,int(n)):
        numCols = i
        numFilas = round(len(cadena) / i)
        entrada.seek(0)
        matrix = []
        
        for k in range(0,numFilas):
            tupla = []
            for p in range(0,i):
                caracter = entrada.readline(1)
                if caracter != " " and caracter != '\n' and caracter != '':
                    tupla.append(caracter)
            matrix.append(tupla)
         
        media = 0
        #Aplicar Indice de coincidencia con matriz cargada.
        for col in range(0,i):

            lista = []
            for fila in matrix:
                if len(fila) == i:
                    lista.append(fila[col])
            total = 26
            listaUnic = pd.unique(lista)
            probTotal = 0
            probSum = 0

            for ele in listaUnic:
                FrecEle = lista.count(ele)
                ftot = FrecEle/len(lista)
                probSum = probSum + ftot * ftot


            media =  media + probSum
            
        media = media / i
        listaMedias.append([i,media])
        print("para clave de tamanio "+ str(i) + ", el indice de coincidencia medio es: " + "{:.4f}".format(media))

    listaMedias.sort(key = lambda x: x[1]) 
    tup = listaMedias[len(listaMedias)-1]
    print("\n-----------------")
    print("el tamanio de clave posiblemente sea: " + str(tup[0]) + " Con un I.C = " + "{:.4f}".format(tup[1]))
    print("-----------------\n")
