import os
import math
from pickle import FALSE
from tkinter import N
import numpy as np
from textos import Textos
from matrizLlave import MatrizLlave

class Hill:

    texto = Textos()                    
    llave = ""                          #   Llave en forma de texto
    n = 0                               #   Tamano de matriz llave n*n cuadrada
    m = 0                               #   Tamano en matriz texto n*m 
    padding = 0                         #   Cantidad de caracteres agregados para rellenar matriz
    matrizTexto = []                  
    matrizLlave = []
    textoCifradoNumerico = []
    textoDecifradoNumerico = []
    matrizLlaveInversa = None           #   Objeto tipo matrizLlave


    def __init__(self, modo = True):
        self.leerLlave()
        self.crearMatrizLlave()
        self.convertirTextoMatriz()

        if(modo):
            self.encriptar()
        else:
            self.desencriptar()

        self.texto.imprimirTextos(modo, self.padding)


    def leerLlave(self):
        fichero = open(os.getcwd()+"/ficheros/llaveHill.txt")
        while 1:
            char = fichero.read(1).lower()         
            if not char:
                break
            if char != " " and char.isalpha():
                self.llave += char


    def crearMatrizLlave(self):
        self.n = math.sqrt(len(self.llave))
        if(not self.n.is_integer()):
            raise ValueError('La llave utilizada para el cifrado de hill debe de poder ser convertible a una matriz de tamaño n * n.')
        
        self.n = int(self.n)
        for i in range (self.n):
            fila = []
            for j in range (self.n):
                fila.append(self.texto.mapa[self.llave[i*self.n + j]])
            self.matrizLlave.append(fila)
        
        self.matrizLlaveInversa = MatrizLlave(self.matrizLlave)


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
                self.textoCifradoNumerico.append(num%26)
        self.texto.numericoConvertirTexto(self.textoCifradoNumerico)
    

    def desencriptar(self):

        self.matrizLlaveInversa.inversa()
        
        # Multiplicar texto cifrado por matriz llave
        for i in range (self.m):
            for j in range (self.n):
                num = 0
                for k in range (self.n):
                    num += self.matrizTexto[k][i] * self.matrizLlaveInversa.matrizInversa[j][k]
                self.textoDecifradoNumerico.append(num%26)
        self.texto.numericoConvertirTexto(self.textoDecifradoNumerico)
        

prueba = Hill()