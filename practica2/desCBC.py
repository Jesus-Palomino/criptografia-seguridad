import argparse
from curses import KEY_BACKSPACE
from operator import concat
import os
from re import M
import numpy as np
from operator import xor
import desStandart

input = "plaintextDES.txt"
output = "output.txt"

print("-----------\nDES version CBC\n-----------\npython3 desCBC.py --help  Para obtener ayuda\n")

parser = argparse.ArgumentParser(description='Parse the func action')
parser.add_argument('--mode', dest='mode', nargs='+', default=False,
                        help='indica el modo de ejecucion --mode D para descifrar y --mode C para cifrar')
parser.add_argument('--k', dest='clave', nargs='+', default=False,
                        help='indica la clave')
parser.add_argument('--iv', dest='vectoriIni', nargs='+', default=False,
                        help='indica el vector de inicialización')
parser.add_argument('--i', dest='i', nargs='+', default=False,
                        help='indica el nombre del fichero input')
parser.add_argument('--o', dest='o', nargs='+', default=False,
                        help='indica el nombre del fichero output')
args = parser.parse_args()

if args.mode:
    if args.mode[0] == 'C':
        print("Modo Cifrado")
        mode = 0 #Modo cifrar
    else:
        print("Modo Descifrado")
        mode = 1 #Modo descifrar

# n = numero de letras
if args.clave:
    clave = args.clave[0]

if args.vectoriIni:
    vectorIni = args.vectoriIni[0]

entrada = open(os.getcwd()+"/ficheros/" + input)
caracter = " "

sal = open(os.getcwd()+"/ficheros/" + output, mode='a')
caracter = " "

keyfile = open(os.getcwd()+"/ficheros/clave.txt")
key = " "


Mtext = []
Mtext_ini = []

ivv = open(os.getcwd()+"/ficheros/IV.txt")
iv = " "

IV = []
PlainText =[]
Key = []

while caracter != "":
    caracter = entrada.readline(1)
    #En caso de que sea letra
    if caracter != " " and caracter != '\n' and caracter != '':
        Mtext_ini.append(caracter)

#Leo caracter a caracter
while iv != "":
    iv = ivv.readline(1)
    #En caso de que sea letra
    if iv != " " and iv != '\n' and iv != '':
        IV.append(iv)
#Leo caracter a caracter
while key != "":
    key = keyfile.readline(1)
    #En caso de que sea letra
    if key != " " and key != '\n' and key != '':
        Key.append(key)
indexAlt = 64
indexLow = 0
sal_siguiente = 0
vectores = []
vectores.append(IV)
indiceVectores = 1
while indexAlt <= (len(Mtext_ini)+63):
    if indexAlt > len(Mtext_ini):
        while len(Mtext_ini) != indexAlt:
            Mtext_ini.insert(0, '0')
    Mtext = Mtext_ini[indexLow:indexAlt]

    print('Bloque a cifrar/descifrar:' )
    print("".join(Mtext))
    vectores.append(Mtext)
    IV = vectores[indiceVectores-1]
    if mode == 0:
        print('IV:')
        print("".join(IV))
    #Tengo el primer bloque, lo cifro:

    if mode == 0:
        Mtext_aux = []
        for i in range(0, len(Mtext)):
            suma = (int(Mtext[i]) + int(IV[i])) % 2
            Mtext_aux.append(str(suma))
        print('Tras sumarle IV: ')
        print("".join(Mtext_aux))
    else:
        Mtext_aux = Mtext
       
    salida = desStandart.des.init(mode,Key, Mtext_aux)

    if mode == 1:
        print('IV:')
        print("".join(IV))

    if mode == 1:
        Mtext_aux = []
        for i in range(0, len(salida)):
            suma_sal = (int(salida[i]) + int(IV[i])) % 2
            Mtext_aux.append(str(suma_sal))
        PlainText = Mtext_aux

    if mode == 0:
        sal.write("".join(salida))
        sal.write("\n")
        print('Salida: ')
        print("".join(salida))

    else:   
        print('Salida: ')
        print("".join(PlainText))
        sal.write("".join(PlainText))
        sal.write("\n")
    indexAlt = indexAlt + 64
    indexLow = indexLow + 64
    indiceVectores = indiceVectores +1