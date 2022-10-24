import argparse
import os
import math
from pickle import FALSE
from tkinter import N
import numpy as np
from textos import Textos
from matrizLlave import MatrizLlave

class Hill:

    texto = None                    
    llave = ""                          #   Llave en forma de texto
    n = 0                               #   Tamano de matriz llave n*n cuadrada
    m = 0                               #   Tamano en matriz texto n*m
    c = 0                               #   Cardinalidad del texto
    padding = 0                         #   Cantidad de caracteres agregados para rellenar matriz
    matrizTexto = []                  
    matrizLlave = []
    textoCifradoNumerico = []
    textoDecifradoNumerico = []
    matrizLlaveInversa = None           #   Objeto tipo matrizLlave


    def __init__(self, mode, c, n, ficheroLlave, input, output):

        self.texto = Textos(input, output)

        self.n = n
        self.c = c

        self.leerLlave(ficheroLlave)
        self.crearMatrizLlave()
        self.convertirTextoMatriz()

        if(mode):
            self.encriptar()
        else:
            self.desencriptar()

        self.texto.imprimirTextos(mode)


    def leerLlave(self, ficheroLlave):
        fichero = open(os.getcwd()+"/ficheros/"+ficheroLlave)
        while 1:
            char = fichero.read(1).lower()         
            if not char:
                break
            if char != " " and char.isalpha():
                self.llave += char


    def crearMatrizLlave(self):
        n = math.sqrt(len(self.llave))
        if(not n.is_integer()):
            raise ValueError('La llave utilizada para el cifrado de hill debe de poder ser convertible a una matriz de tamaño n * n.')

        if(n != self.n):
            raise ValueError('La dimension de la matriz de transformacion especificada no coincide con la dimension de la matriz dentro del fichero dado')
        
        self.n = int(self.n)
        for i in range (self.n):
            fila = []
            for j in range (self.n):
                fila.append(self.texto.mapa[self.llave[i*self.n + j]])
            self.matrizLlave.append(fila)
        
        self.matrizLlaveInversa = MatrizLlave(self.matrizLlave, self.c)


    def convertirTextoMatriz(self):
        self.padding = len(self.texto.textoNumerico) % self.n
        if(self.padding):
            self.padding = self.n - self.padding

        m = len(self.texto.textoNumerico) / self.n
        if(not m.is_integer()):
            m += 1
        self.m = int(m)

        matrizTemporal = [[0 for x in range(self.m)] for y in range(self.n)]

        index = 0
        leng = len(self.texto.textoNumerico)
        for i in range(self.m):
            for j in range(self.n):
                if(index < leng):
                    matrizTemporal[j][i] = self.texto.textoNumerico[index]
                    index+= 1

        self.matrizTexto = matrizTemporal


    def encriptar(self):
        # Matrix llave (n*n) por matriz texto(n*m) 
        for i in range (self.m):
            for j in range (self.n):
                num = 0
                for k in range (self.n):
                    num += self.matrizTexto[k][i] * self.matrizLlave[j][k]
                self.textoCifradoNumerico.append(num%self.c)
        self.texto.numericoConvertirTexto(self.textoCifradoNumerico)
    

    def desencriptar(self):

        self.matrizLlaveInversa.inversa()
        
        # Multiplicar texto cifrado por matriz llave
        for i in range (self.m):
            for j in range (self.n):
                num = 0
                for k in range (self.n):
                    num += self.matrizTexto[k][i] * self.matrizLlaveInversa.matrizInversa[j][k]
                self.textoDecifradoNumerico.append(num%self.c)
        self.texto.numericoConvertirTexto(self.textoDecifradoNumerico)


print("\n----------------------\nMETODO HILL\n----------------------\npython hill.py --help  Para obtener ayuda\n")

parser = argparse.ArgumentParser(description='Parse the func action')
parser.add_argument('--mode', dest='mode', nargs='+', default=False,
                        help='indica el modo de ejecucion --mode D para descifrar y --mode C para cifrar')
parser.add_argument('--m', dest='size', nargs='+', default=False,
                        help='indica la cardinalidad del texto')
parser.add_argument('--n', dest='dimension', nargs='+', default=False,
                        help='indica la dimension de la matriz de transformacion')
parser.add_argument('--k', dest='key', nargs='+', default=False,
                        help='indica el nombre del fichero con la matriz de transformacion')                   
parser.add_argument('--i', dest='i', nargs='+', default=False,
                        help='indica el nombre del fichero input')
parser.add_argument('--o', dest='o', nargs='+', default=False,
                        help='indica el nombre del fichero output')
args = parser.parse_args()


if args.mode:
    if args.mode[0] == 'C':
        print("Modo Cifrado\n")
        mode = 1 #Modo cifrar
    else:
        print("Modo Descifrado\n")
        mode = 0 #Modo descifrar

# Cardinalidad del lenguaje
if args.size:
    c = int(args.size[0])

# Dimension de matriz de transformacion
if args.dimension:
    n = int(args.dimension[0])

# Nombre fichero con matriz de transformacion
if args.key:
    ficheroLlave = args.key[0]

# Nombre fichero de input
if args.i:
    input = args.i[0]

# Nombre fichero de output
if args.o:
    output = args.o[0]


if not args.mode or not args.size or not args.dimension or not args.key or not args.i or not args.o:
    print("Error en formato de entrada. Ejemplo de formato correcto:\npython hill.py --mode C --m 26 --n 3 --k llaveHill.txt --i input.txt --o output.txt\n")
    exit(0)


prueba = Hill(mode, c, n, ficheroLlave, input, output)