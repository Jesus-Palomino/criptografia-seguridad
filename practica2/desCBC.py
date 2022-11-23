import argparse
import random
from curses import KEY_BACKSPACE
from operator import concat
import os
from re import M
import numpy as np
from operator import xor
import desStandart
from os import sys
import convertirBinario

input = "/ficheros/plaintextDES.txt"
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

if args.vectoriIni:
    vectorIni = args.vectoriIni[0]

if args.i:
    i = args.i[0]
    if mode == 0:
        bina = convertirBinario.convertirBinario()
        if 'imagenes' in i:
            #Procesar imagen
            imgbin = bina.image_to_bits(i)
            input = '/ficheros/binario.txt'

        if 'textos' in i:
            #Procesar textos
            textbin = bina.text_to_bits(i)
            input = '/ficheros/binario.txt'
    else:
        bina = convertirBinario.convertirBinario()
        input = i


entrada = open(os.getcwd()+ input)
caracter = " "

if mode == 0:
    contadorPadding = open(os.getcwd()+"/ficheros/contadorPadding.txt", 'w')
else:
    contadorPadding = open(os.getcwd()+"/ficheros/contadorPadding.txt", 'r')
    contPad = int(contadorPadding.read())

sal = open(os.getcwd()+"/ficheros/" + output,'w').close()
sal = open(os.getcwd()+"/ficheros/" + output, mode='a')
caracter = " "

if args.clave:
    clave = args.clave[0]
    keyfile = open(os.getcwd()+"/ficheros/clave.txt")
    key = " "
    Key = []
    #Leo caracter a caracter
    while key != "":
        key = keyfile.readline(1)
        #En caso de que sea letra
        if key != " " and key != '\n' and key != '':
            Key.append(key)
    contadorParidad = 0
    bloq1 = []
    bloq1.append(Key[0:8])
    bloq1.append(Key[8:16])
    bloq1.append(Key[16:24])
    bloq1.append(Key[24:32])
    bloq1.append(Key[32:40])
    bloq1.append(Key[40:48])
    bloq1.append(Key[48:56])
    bloq1.append(Key[56:64])

    for b in bloq1:
        contadorParidad = b.count('1')

        if contadorParidad % 2 == 0:
            print('La clave no cumple los criterios de paridad')
            sys.exit()
else:
    Key = []
    for j in range(8):
        lstAux = []
        #Genero aleatoriamente la clave
        for i in range(7):
            # randint function to generate
            # 0, 1 randomly and converting
            # the result into str
            temp = str(random.randint(0, 1))
            # Concatenation the random 0, 1
            # to the final result
            Key.append(temp)
            lstAux.append(temp)
        counterPari = lstAux.count('1')
        if counterPari%2== 0:
            Key.append('1')
        else:
            Key.append('0')
    print('Clave generada de forma automatica cumpliendo requisitos de paridad:')
    print("".join(Key)+'\n\n')


Mtext = []
Mtext_ini = []

ivv = open(os.getcwd()+"/ficheros/IV.txt")
iv = " "

IV = []
PlainText =[]

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

        
contadorPaddingax = 0
contBloq = 1
indexAlt = 64
indexLow = 0
sal_siguiente = 0
vectores = []
vectores.append(IV)
indiceVectores = 1
textoCifrado = []

if mode == 0:
    while len(Mtext_ini)%64 != 0:
        contadorPaddingax+=1
        Mtext_ini.insert(0, '0')

while indexAlt <= (len(Mtext_ini)+63):

    Mtext = Mtext_ini[indexLow:indexAlt]

    #print('Cifrando Bloque '+  str(contBloq)+'....')
    #print("".join(Mtext))
    if mode != 0:
        vectores.append(Mtext)

    IV = vectores[indiceVectores-1]
    # if mode == 0:
    #     print('IV:')
    #     print("".join(IV))
    #Tengo el primer bloque, lo cifro:

    if mode == 0:
        Mtext_aux = []
        for i in range(0, len(Mtext)):
            suma = (int(Mtext[i]) + int(IV[i])) % 2
            Mtext_aux.append(str(suma))
        # print('Tras sumarle IV: ')
        # print("".join(Mtext_aux))
    else:
        Mtext_aux = Mtext
       
    salida = desStandart.des.init(mode,Key, Mtext_aux)

    if mode == 0:
        vectores.append(salida)

    if mode == 1:
        Mtext_aux = []
        for i in range(0, len(salida)):
            suma_sal = (int(salida[i]) + int(IV[i])) % 2
            Mtext_aux.append(str(suma_sal))
        PlainText = Mtext_aux

    if mode == 0:
        sal.write("".join(salida))
        sal.write("\n")
        #print('----> OK !')
        textoCifrado.append("".join(salida))
        # print('Salida: ')
        # print("".join(salida))

    else:   
        # print('Salida: ')
        # print("".join(PlainText))
        sal.write("".join(PlainText))
        textoCifrado.append("".join(PlainText))
        sal.write("\n")
        #print('----> OK !')
    indexAlt = indexAlt + 64
    indexLow = indexLow + 64
    indiceVectores = indiceVectores +1
    contBloq+= 1

if mode == 0:
    print('\nTexto Claro:')
    print("".join(Mtext_ini))
    print('------------------------------------')
    print('Texto Cifrado')
    print("".join(textoCifrado))
    contadorPadding.write(str(contadorPaddingax))
    sal.close()
    out = open(os.getcwd()+"/ficheros/" + output,'r')
    auxout = out.read()
    out.close()
    if args.i:
        if 'imagenes' in args.i[0]:
            #Procesar imagen
            out = open(os.getcwd()+"/imagenes/imagenCifrada.txt",'w')
            out.write(auxout)

        if 'textos' in args.i[0]:
            #Procesar textos
            out = open(os.getcwd()+"/textos/textoCifrado.txt",'w')
            out.write(auxout)

            


else:
    print('Texto Cifrado:')
    print("".join(Mtext_ini))
    print('------------------------------------')
    print('Texto Claro')
    print("".join(textoCifrado))
    sal.close()

    out = open(os.getcwd()+"/ficheros/" + output,'r')
    auxout = out.read()
    auxout = auxout.replace('\n', '')
    realout = auxout[contPad:]
    out.close()

    out = open(os.getcwd()+"/ficheros/" + output,'w')
    out.write(realout)
    out.close()

    if args.i:
        if 'imagenes' in args.i[0]:
            #Procesar imagen
            imgbin = bina.bits_to_image('ficheros/output.txt', imagen='/imagenes/imagenClaro.jpg')

        if 'textos' in args.i[0]:
            #Procesar textos
            textbin = bina.bits_to_text('ficheros/output.txt', texto='textos/textoClaro.txt')
