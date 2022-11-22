from cifradoDesplazamiento import CifradoDesplazamiento

from random import seed
from random import randint
from collections import Counter
from decimal import Decimal, ROUND_DOWN

import os
import argparse


class seguridadPerfecta:

    metodo = None
    llave = []

    n = None
    size = 0

    reps_texto_plano = None
    reps_texto_cifrado = None
    dicc_probs = None
    probs_texto_cifrado = None
    
    ficheroOutput = ""

    def __init__(self, modo, input, output, n = 26):

        self.n = n
        self.ficheroOutput = output

        self.metodo = CifradoDesplazamiento(input, output, n)

        self.size = len(self.metodo.texto.textoPlano)

        if(modo):
            self.generarLlaveEquiprobable()
        else:
            self.generarLlaveNoEquiprobable()
        
        self.metodo.cifrado(self.llave)

        self.reps_texto_plano = self.calcularRepeticiones(self.metodo.texto.textoPlano)
        self.reps_texto_cifrado = self.calcularRepeticiones(self.metodo.texto.textoProcesado)

        self.probabilidadCondicionada()
        self.probs_texto_plano = self.probabilidad_caracter(self.reps_texto_plano)
        self.imprimir()


    def generarLlaveEquiprobable(self):
        seed(1)
        for i in range(self.size):
            self.llave.append(randint(1, self.n))

    def generarLlaveNoEquiprobable(self):
        # Llave en la que el primer caracter del lenguaje ('a') tiene una probabilidad fija del 10%
        seed(1)
        for i in range(self.size):
            if(randint(1, 10) == 1):
                self.llave.append(1)
            else:
                self.llave.append(randint(1, self.n))
        pass

    def calcularRepeticiones(self, lista):
        # Diccionario de cantidad de apariciones por cada caracter
        dic_probabilidad = Counter(lista)

        return dic_probabilidad

    def probabilidadCondicionada(self):
        # Diccionario de diccionarios
        dicc_probs = dict()
        temp = dict()
        
        for char in self.metodo.texto.abecedario:
            temp[char] = 0

        for char in self.metodo.texto.abecedario:
            dicc_probs[char] = temp.copy()

        for i in range(self.size):
            dicc_probs[self.metodo.texto.textoPlano[i]][self.metodo.texto.textoProcesado[i]] += 1

        for char in self.metodo.texto.abecedario:
            for char2 in self.metodo.texto.abecedario:
                if (self.reps_texto_cifrado[char] != 0):
                    dicc_probs[char][char2] = format(dicc_probs[char][char2] / self.reps_texto_cifrado[char], '.15f')
                    
        
        self.dicc_probs = dicc_probs


    def probabilidad_caracter(self, dict):
        # Probabilidad de apariciones
        temp = dict.copy()
        for key in temp:
            temp[key] = temp[key] / self.size
        
        return temp
    
    def imprimir(self):

        fichero = open(os.getcwd()+"/ficheros/" + self.ficheroOutput, 'w')

        for char in self.metodo.texto.abecedario:
            fichero.write("".join("P(" + char.upper() + ") = " + str(format(self.probs_texto_plano[char], '.15f'))))
            fichero.write("\n")
        
        fichero.write("\n")
        for char in self.metodo.texto.abecedario:
            for char2 in self.metodo.texto.abecedario:
                fichero.write("".join("P(" + char.upper() + "|" + char2.upper() + ") = " + str(self.dicc_probs[char][char2]) + "\t"))
            fichero.write("\n")



print("Comprobacion empirica de la Seguridad Perfecta del cifrado por desplazamiento\n")
print("python seguridadPerfecta.py --help  Para obtener ayuda\n")

parser = argparse.ArgumentParser(description='Parse the func action')
parser.add_argument('--llave', dest='mode', nargs='+', default=False,
                        help='indica el modo de generacion de la clave --llave P para clave equiprobable y --llave I para clave no equiprobable')
parser.add_argument('--m', dest='size', nargs='+', default=False,
                        help='indica la cardinalidad del texto')            
parser.add_argument('--i', dest='i', nargs='+', default=False,
                        help='indica el nombre del fichero input')
parser.add_argument('--o', dest='o', nargs='+', default=False,
                        help='indica el nombre del fichero output')
args = parser.parse_args()


if args.mode:
    if args.mode[0] == 'P':
        print("Uso de clave equiprobable para cifrado\n")
        mode = 1
    else:
        print("Uso de clave no equiprobable para cifrado\n")
        mode = 0

# Cardinalidad del lenguaje
if args.size:
    c = int(args.size[0])

# Nombre fichero de input
if args.i:
    input = args.i[0]

# Nombre fichero de output
if args.o:
    output = args.o[0]


if not args.mode or not args.size or not args.i or not args.o:
    print("Error en formato de entrada. Ejemplo de formato correcto: ")
    print("python seguridadPerfecta.py --llave P --m 26 --i texto.txt --o probabilidades.txt\n")
    exit(0)

seguridadPerfecta(mode, input, output, c)