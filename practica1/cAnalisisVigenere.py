import argparse
from ctypes import sizeof
from fileinput import close
import os
import string
from gmpy2 import mpz
from euclides_extendido import inverso_multiplicativo


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
                        help='indica el nombre del fichero input')
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

#Modo kasiski
if mode == 0:
    entrada = open(os.getcwd()+"/ficheros/" + input)
    caracter = " "
    cadena = entrada.read()

    for i in range(2,int(n)):
        print("Probando con cadenas de " + str(i) + " Caractres")
        entradaAux = cadena
        distancias = []
        buscador = entradaAux[0:i]
        entradaAux = cadena[i+1:]
        contador = entradaAux.count(buscador)
        distancia = 0
        print("----------")
        while contador != 0:
            
            contador = entradaAux.count(buscador)
            distancia = entradaAux.find(buscador) +1
            entradaAux = entradaAux[distancia:]
            if len(distancias) > 0:
                distancia = distancia + distancias[0]
            print("Distancia de la ocurrencia: " + str(distancia))
            distancias.append(distancia)
        print("----------")
        for l in distancias:
            if contador > 0:
                listaMul = []
                for i in range(1,distancia+1):
                    if distancia%i == 0:
                        listaMul.append(i)


                print(listaMul)    

