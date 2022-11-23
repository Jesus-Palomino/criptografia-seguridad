import argparse
import random
import os
from re import M
import desStandart
from os import sys
import convertirBinario

input = "/ficheros/plaintextDES.txt"
output = "output.txt"

print("-----------\nDES version CBC\n-----------\npython3 desCBC.py --help  Para obtener ayuda\n")

parser = argparse.ArgumentParser(description='Parse the func action')
parser.add_argument('--mode', dest='mode', nargs='+', default=False,
                        help='indica el modo de ejecucion --mode D para descifrar y --mode C para cifrar')
parser.add_argument('--k1', dest='clave', nargs='+', default=False,
                        help='indica la clave')

parser.add_argument('--s', dest='size', nargs='+', default=False,
                        help='indica el tamanyo de bloque')
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

if args.size:
    size = int(args.size[0])

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

if args.clave:
    clave = args.clave[0]
    keyfile = open(os.getcwd()+"/ficheros/clave.txt")
    key = " "
    Key = []
    contadorParidad = []
    #Leo caracter a caracter
    while key != "":
        key = keyfile.readline(1)
        #En caso de que sea letra
        if key != " " and key != '\n' and key != '':
            Key.append(key)
    for j in range(3):
        if j == 0:
            plus = 0
        if j == 1:
            plus = 64
        if j == 2:
            plus = 128
        contadorParidad.append(0)
        bloq1 = []
        bloq1.append(Key[0+plus:8+plus])
        bloq1.append(Key[8+plus:16+plus])
        bloq1.append(Key[16+plus:24+plus])
        bloq1.append(Key[24+plus:32+plus])
        bloq1.append(Key[32+plus:40+plus])
        bloq1.append(Key[40+plus:48+plus])
        bloq1.append(Key[48+plus:56+plus])
        bloq1.append(Key[56+plus:64+plus])

        for b in bloq1:
            contadorParidadls = b.count('1')
            
            if contadorParidadls % 2 == 0:
                print('La clave no cumple los criterios de paridad')
                sys.exit()


else:
    Key = []
    for k in range(3):
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
    print('k1: ' + "".join(Key[0:64]))
    print('k2: ' + "".join(Key[64:128]))
    print('k3: ' + "".join(Key[128:])+'\n')
            

entrada = open(os.getcwd()+input)
caracter = " "

open(os.getcwd()+"/ficheros/" + output, 'w').close()
sal = open(os.getcwd()+"/ficheros/" + output, mode='a')
caracter = " "

if mode == 0:
    contadorPadding = open(os.getcwd()+"/ficheros/contadorPadding.txt", 'w')
else:
    contadorPadding = open(os.getcwd()+"/ficheros/contadorPadding.txt", 'r')
    contPad = int(contadorPadding.read())

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


vectores = []
vectores.append(IV)
listKeys = []

key1 = Key[0:64]
key2 = Key[64:128]
key3 = Key[128:192]


listKeys.append(key1)
listKeys.append(key2)
listKeys.append(key3)

contadorPaddingax=0
if mode == 0:
    while len(Mtext_ini)%64 != 0:
        contadorPaddingax+=1
        Mtext_ini.insert(0, '0')


solu = []
Mtext_aux2 = []
for paso in range(0,3):
    if paso != 0:
        Mtext_ini = "".join(Mtext_aux2)
    indexAlt = size
    indexLow = 0
    indiceVectores = 1

    Mtext_aux2 = []

    if paso == 0:
        print("------------\nPrimer Cifrado DES\n--------------")
    if paso == 1:
        print("------------\nPrimer Descifrado DES\n--------------")
    if paso == 2:
        print("------------\nSegundo Cifrado DES\n--------------")

        
    while indexAlt <= (len(Mtext_ini)+size):
        # if indexAlt > len(Mtext_ini):
        #     while len(Mtext_ini) != indexAlt:
        #         Mtext_ini.insert(0, '0')
        
        Mtext = Mtext_ini[indexLow:indexAlt]

        IV = vectores[indiceVectores-1]
        #print('Cifrando bloque: ' + str(indiceVectores) + '....... ' )
        # print("".join(Mtext))

        # print('IV: ' )
        # print("".join(IV))

        #Shift Box
        while len(IV) < 64:
            IV.append('0')
        # print('Insertamos ceros a IV: ' )
        # print("".join(IV))
        # print(len(listKeys))
        # print(paso)
            
        #Seleccion cifrado descifrado
        if mode == 0:
            key = listKeys[paso]
        else:
            key = listKeys[2-paso]
            
        if paso == 1:
            salida = desStandart.des.init(0, key, IV)
        else:
            salida = desStandart.des.init(0,key, IV)

        # print('Pasamos por DeS' )
        # print("".join(salida))
        
        #Seleccion de bits
        salida = salida[0:size]    

        # print('Selecciono Bits' )
        # print("".join(salida))

        #if mode == 0:
        Mtext_aux = []
        for i in range(0, len(Mtext)):
            suma = (int(Mtext[i]) + int(salida[i])) % 2
            Mtext_aux.append(str(suma))
        # print('Tras sumarle plaintext: ')
        # print("".join(Mtext_aux))
        # else:
        #     Mtext_aux = Mtext

        #IV del siguiente bloque
        if mode == 0:
            vectores.append(Mtext_aux)
        else:
            vectores.append(Mtext)
        # if mode == 1:
        #     print('IV:')
        #     print("".join(IV))

        # if mode == 1:
        #     Mtext_aux = []
        #     for i in range(0, len(salida)):
        #         suma_sal = (int(salida[i]) + int(IV[i])) % 2
        #         Mtext_aux.append(str(suma_sal))
        #     PlainText = Mtext_aux
        
        if paso == 2:
            sal.write("".join(Mtext_aux))
            sal.write("\n")
            solu.append("".join(Mtext_aux))
        # print('Salida: ')
        # print("".join(Mtext_aux))
        Mtext_aux2.append("".join(Mtext_aux))
        indexAlt = indexAlt + size
        indexLow = indexLow + size
        indiceVectores = indiceVectores +1
        #print('-----> OK!')

        

if mode == 0:
    print('\nTexto Claro:')
    print("".join(Mtext_ini))
    print('------------------------------------')
    print('Texto Cifrado')
    print("".join(solu))
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
    print("".join(solu))
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
