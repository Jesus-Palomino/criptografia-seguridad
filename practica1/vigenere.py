import argparse
from fileinput import close
import os
import string
from gmpy2 import mpz
from euclides_extendido import inverso_multiplicativo


#EJECUCION:
#   python afin.py --mode C --m 26 --a 15 --b hola --i input.txt --o output.txt
print("--------------\nCIFRADO VIGENERE\n--------------\npython vigenere.py --help  Para obtener ayuda\n")

abecedario = list(string.ascii_lowercase)
input = "input.txt"
output = "output.txt"
size = 26

parser = argparse.ArgumentParser(description='Parse the func action')
parser.add_argument('--mode', dest='mode', nargs='+', default=False,
                        help='indica el modo de ejecucion --mode D para descifrar y --mode C para cifrar')
parser.add_argument('--k', dest='k', nargs='+', default=False,
                        help='indica la clave')
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

# k = coeficiente multiplicato
if args.k:
    k = args.k[0]

if args.i:
    input = args.i[0]

if args.o:
    output = args.o[0]

if not args.mode or not k:
    print("Error en formato de entrada. Ejemplo de formato correcto:\npython afin.py --mode C --m 26 --a 5 --b clave --i input.txt --o output.txt")
    exit(0)



entrada = open(os.getcwd()+"/ficheros/" + input)
caracter = " "


#Cifrado:
if mode == 0:
    caracterNumerico = []
    listaAux = []
    caractCif = []
    #Leo caracter a caracter
    while caracter != "":
        caracter = entrada.readline(1)
        #En caso de que sea letra
        if caracter != " " and caracter != '\n' and caracter != '':
            #anyado a una lista el valor numerico
            listaAux.append(caracter)
            caracterNumerico.append(abecedario.index(caracter)+1)
    entrada.close()
    print("\nTexto Claro:")
    print("".join(listaAux))
    indice = 0

    for i in caracterNumerico:
        #aplico formula
        #Si ha llegado al final de la clave, vuelve al principio
        if indice >= len(k):
            indice = 0
        #Si no, guardo el asci del caracter de la clave
        newB = abecedario.index(k[indice]) + 1
        indice = indice + 1

        cif = (int(i) + int(newB)) % int(size)
        #anyado a lista el valor textual
        caractCif.append(abecedario[cif-1])
        

    salida = open(os.getcwd()+"/ficheros/" + output, 'w')
    salida.write("".join(caractCif))
    print("//////////////\nTexto Cifrado:")
    print("".join(caractCif) + "\n")


else:

    caracterNumerico = []
    caractCif = []
    listaAux = []
    while caracter != "":
        caracter = entrada.readline(1)
        if caracter != " " and caracter != '\n' and caracter != '':
            caracterNumerico.append(abecedario.index(caracter)+1)
            listaAux.append(caracter)
    entrada.close()
    print("\nTexto Cifrado:")
    print("".join(listaAux))

    indice = 0
    for i in caracterNumerico:
        #Si ha llegado al final de la clave, vuelve al principio
        if indice >= len(k):
            indice = 0
        #Si no, guardo el asci del caracter de la clave
        newB = abecedario.index(k[indice]) + 1
        indice = indice + 1
        cif = (int(i) - int(newB)) % int(size)
        caractCif.append(abecedario[cif-1])

    salida = open(os.getcwd()+"/ficheros/" + output, 'w')
    salida.write("".join(caractCif))
    salida.close()
    print("//////////////\nTexto Claro:")
    print("".join(caractCif) + "\n")


def test_kasiski():
    return